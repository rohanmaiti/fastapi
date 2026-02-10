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
async def signup(data: SignupModel):
    return

@router.post('/login')
async def login(response: Response, data: LoginModel, session: AsyncSession = Depends(get_session)):
    stmt = select(Users).where(
        Users.email == data.email,
        Users.password == data.password
    )

    result = await session.execute(stmt)
    user = result.scalar_one_or_none()

    access_token = create_access_token(user_id = user.id)
    refresh_token = create_refresh_token(user_id= user.id)

    response.set_cookie('refresh_token', refresh_token)

    if (user):
        return {
        "access_token": access_token,
        "refresh_token": refresh_token
        }
    
    raise HTTPException(status_code=400, detail="invalid credentials")
    
    


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