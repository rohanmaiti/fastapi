from fastapi import Response
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
import uuid
from app.core.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, REFRESH_TOKEN_EXPIRE_MINUTES
from fastapi.exceptions import HTTPException


def create_access_token(user_id: str):
    to_encode = {
        "sub": str(user_id)
    }
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    jti = str(uuid.uuid4())   # unique token id
    to_encode.update({
        "exp": expire,
        "jti": jti
    })
    encoded_token = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_token


def create_refresh_token(user_id: str):
    to_encode = {
        "sub": str(user_id)
    }

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=REFRESH_TOKEN_EXPIRE_MINUTES
    )
    jti = str(uuid.uuid4())
    to_encode.update({
        "exp": expire,
        "jti": jti,
        "type": "refresh"
    })

    encoded_token = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_token


async def handle_refresh(response: Response, refresh_token: str):
    try:
        payload = jwt.decode(
            refresh_token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        if payload.get("type") != "refresh":
            raise HTTPException(status_code=401)

        user_id = payload.get("sub")

    except JWTError:
        raise HTTPException(status_code=401)

    new_access = create_access_token(user_id)
    new_refresh = create_refresh_token(user_id)

    response.set_cookie(
        'refresh_token',
        new_refresh,
        httponly=True,
        secure=True,
        samesite='lax',
        max_age=REFRESH_TOKEN_EXPIRE_MINUTES * 60
    )

    return {
        "access_token": new_access,
        "refresh_token": new_refresh
    }

      