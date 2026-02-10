from fastapi import Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select 
from app.db.models import Users



from app.core.config import SECRET_KEY, ALGORITHM
from app.db.deps import get_session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_token(request: Request, token = Depends(oauth2_scheme), session = Depends(get_session)):
    if token:
        return token

    cookie_token = request.cookies.get('access_token')
    if cookie_token:
        return cookie_token

    raise HTTPException(status_code=401, detail="Unauthorized")


def get_refresh_token(request: Request):
    return request.cookies.get('refresh_token')


could_not_validate_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"})


async def get_current_user(
        token = Depends(get_token),
        session = Depends(get_session)
):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        user_id: str = str(payload.get("sub") or payload["sub"])
        if (user_id) is None:
            raise could_not_validate_exception
        
        stmt = select(Users).where(Users.id == (user_id))
        result = await session.execute(stmt)
        user = result.scalar_one_or_none()

        if user is None:
            raise could_not_validate_exception
        
        return {
            "data": {
            "name": user['first_name'],
            "email": user["email"]
            },
            "status": "200",
            "message":"login successfull"
        }
    
    except JWTError: 
        raise could_not_validate_exception