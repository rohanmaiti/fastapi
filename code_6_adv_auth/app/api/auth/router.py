from fastapi import APIRouter
from pydantic import BaseModel
from app.api.auth.schemas.request import *



router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/signup")
async def signup(data: SignupModel ):
    return

@router.post('/login')
async def login(data: LoginModel):
    return

@router.post('/refresh')
async def refresh(token: str):
    return 