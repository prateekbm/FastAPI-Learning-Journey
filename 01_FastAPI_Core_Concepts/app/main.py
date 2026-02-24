from fastapi import FastAPI, HTTPException, Query
from typing import List
from .schemas import ItemCreate, ItemResponse
from .models import Item
from .database import items_db
app = FastAPI(title="FastAPI Core Concepts API")

@app.post("/items/", response_model=ItemResponse)
def create_item(item: ItemCreate):
    new_item = Item(id=len(items_db)+1, **item.model_dump())
    items_db.append(new_item)
    return new_item

@app.get("/items/", response_model=List[ItemResponse])
def get_items(min_price: float = Query(None, gt=0)):
    if min_price:
        return [item for item in items_db if item.price >= min_price]
    return items_db

@app.get("/items/{item_id}", response_model=ItemResponse)
def get_item(item_id: int):
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, updated_item: ItemCreate):
    for index, item in enumerate(items_db):
        if item.id == item_id:
            new_item = Item(id=item_id, **updated_item.model_dump())
            items_db[index] = new_item
            return new_item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(items_db):
        if item.id == item_id:
            items_db.pop(index)
            return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")