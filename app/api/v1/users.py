from fastapi import APIRouter
from app.core.security import create_token

router = APIRouter()

@router.post("/login")
def login(username: str):
    token = create_token({"sub": username})
    return {"access_token": token}
