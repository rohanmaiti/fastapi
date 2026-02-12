from fastapi import APIRouter, Depends, Response, Request
from pydantic import BaseModel
from typing import Optional
from app.db.models import Users;
from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.deps import get_session
from fastapi.exceptions import HTTPException
from app.core.jwt import create_access_token, create_refresh_token
from app.core.jwt import handle_refresh
from app.core.deps import get_current_user
from app.core.config import REFRESH_TOKEN_EXPIRE_MINUTES

class SignupModel(BaseModel):
    email: str
    password: str
    name: Optional[str]
    

class LoginModel(BaseModel):
    email: str
    password: str


class RefreshModel(BaseModel):
    refresh_token: Optional[str]
    


router = APIRouter(prefix='/auth')

@router.post('/signup')
async def signup(data: SignupModel, session: AsyncSession = Depends(get_session)):
    from app.core.security import hash_password
    
    # Check if user already exists
    stmt = select(Users).where(Users.email == data.email)
    result = await session.execute(stmt)
    existing_user = result.scalar_one_or_none()
    
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Create new user with hashed password
    new_user = Users(
        email=data.email,
        first_name=data.name or data.email.split('@')[0],
        password=hash_password(data.password)
    )
    
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    
    return {
        "message": "User created successfully",
        "user": {
            "id": new_user.id,
            "email": new_user.email,
            "name": new_user.first_name
        }
    }

@router.post('/login')
async def login(response: Response, data: LoginModel, session: AsyncSession = Depends(get_session)):
    from app.core.security import verify_password
    
    # First, find user by email
    stmt = select(Users).where(Users.email == data.email)
    result = await session.execute(stmt)
    user = result.scalar_one_or_none()
    
    # Validate user exists and password is correct
    if not user or not verify_password(data.password, user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    # Create tokens only after validation
    access_token = create_access_token(user_id=user.id)
    refresh_token = create_refresh_token(user_id=user.id)
    
    # Set secure cookie
    response.set_cookie(
        'refresh_token',
        refresh_token,
        httponly=True,
        secure=True,
        samesite='lax',
        max_age=REFRESH_TOKEN_EXPIRE_MINUTES * 60
    )
    
    return {
        "access_token": access_token,
        "refresh_token": refresh_token
    }
    
    


@router.post("/refresh")
async def refresh_token_endpoint(
    response: Response,
    request: Request,
    data: Optional[RefreshModel] = None
):
    refresh_token = (
        data.refresh_token if data and data.refresh_token 
        else request.cookies.get('refresh_token')
    )
    if not refresh_token:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return await handle_refresh(response, refresh_token)




@router.post('/me')
def me(current_user = Depends(get_current_user)):
    return current_user