from fastapi import Header, HTTPException

def verify_token(x_token: str = Header(...)):
    if x_token != "secret-token":
        raise HTTPException(status_code=401, detail="Invalid Token")
    return x_token