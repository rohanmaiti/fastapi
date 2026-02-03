from fastapi import Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from app.core.config import SECRET_KEY, ALGORITHM
from app.db.dependency import get_session
from app.db.models import Users

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login") # this line is for Swagger UI to get token

def get_token(request: Request, token = Depends(oauth2_scheme)):

    #* this line above does the same as the below code --> token = Depends(oauth2_scheme))
    # auth = request.headers.get("Authorization")
    # if auth and auth.startswith("Bearer "):  # Note the space after Bearer
    #     return auth.split(" ")[1]
    
    if token:
        return token
    
    cookie_token = request.cookies.get("jwt_token")

    if cookie_token:
        return cookie_token

    raise HTTPException(status_code=401, detail="Not authenticated")



async def get_current_user(
        token = Depends(get_token),
        session : AsyncSession = Depends(get_session) 
):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        user_id: str = payload.get("sub")

        if user_id is None:
            raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"})

    except JWTError:
        raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    stmt = select(Users).where(Users.id == str(user_id))
    result = await session.execute(stmt)
    user = result.scalar_one_or_none()

    if user is None:
        
        raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
        )
    
    return user

   


