from fastapi import APIRouter, Depends
from .dependencies import verify_token
from .exceptions import CustomException

router = APIRouter()

@router.get("/secure-data")
def secure_data(token: str = Depends(verify_token)):
    return {"message": "Access granted", "token": token}

@router.get("/error/{name}")
def raise_error(name: str):
    raise CustomException(name)