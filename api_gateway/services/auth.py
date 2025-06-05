from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/auth/login")
def login_user(data: LoginRequest):
    if data.username == "client" and data.password == "123":
        return {"token": "fake-jwt-client", "role": "client"}
    if data.username == "chef" and data.password == "123":
        return {"token": "fake-jwt-chef", "role": "chef"}
    if data.username == "livreur" and data.password == "123":
        return {"token": "fake-jwt-livreur", "role": "livreur"}
    return {"error": "Identifiants invalides"}
