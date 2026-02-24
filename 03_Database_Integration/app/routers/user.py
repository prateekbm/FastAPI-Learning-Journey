from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import sessionLocal
from .. import crud, schemas

router=APIRouter(prefix="/users", tags=["Users"])
def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/",response_model=schemas.UserResponse)
def create_user(user:schemas.UserCreate, db:Session=Depends(get_db)):
    return crud.create_user(db, user)

@router.get("/",response_model=list[schemas.UserResponse])
def read_users(db:Session=Depends(get_db)):
    return crud.get_users(db)