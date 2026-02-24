from pydantic import BaseModel, Field

class ItemCreate(BaseModel):
    name: str = Field(..., min_length=2)
    price: float = Field(..., gt=0)
    in_stock: bool

class ItemResponse(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool