from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Optional
from app.db.models import Users;
from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.deps import get_session
from fastapi.exceptions import HTTPException

class SignupModel(BaseModel):
    email: str
    password: str
    name: Optional[str]
    

class LoginModel(BaseModel):
    email: str
    password: str
    


router = APIRouter(prefix='/auth')

@router.post('/signup')
async def signup(data: SignupModel):
    return

@router.post('/login')
async def login(data: LoginModel, session: AsyncSession = Depends(get_session)):
    stmt = select(Users).where(
        Users.email == data.email,
        Users.password == data.password
    )

    result = await session.execute(stmt)
    user = result.scalar_one_or_none()
    if (user):
        return user
    raise HTTPException(status_code=400, detail="invalid credentials")
    
    

@router.post('/me')
async def me():
    return 