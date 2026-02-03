from fastapi.responses import JSONResponse
from app.api.user.v1.request import SingupModel, LoginModel
from sqlalchemy import select 
from app.db.models import Users
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.security import hash_password, verify_password
from fastapi import HTTPException, Response
from app.core.jwt import create_access_token




async def does_user_exists(data: SingupModel,  session: AsyncSession):
    query=select(Users).where(Users.email == data.email)
    result = await session.execute(query)
    existing_user = result.scalar_one_or_none()
    print('existing_user', existing_user)
    print(bool(existing_user))
    return bool(existing_user)



async def insert_user_in_db(data: SingupModel, session: AsyncSession):
    hashed_password = hash_password(data.password)
    new_user = Users(
        email=data.email,
        first_name=data.first_name,
        last_name=data.last_name,
        password=hashed_password
    )
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)

    return JSONResponse(status_code=201, content={
        "message": "User created successfully",
        "data": {
            "email": data.email,
            "first_name": data.first_name
        }
    })


async def handle_login(data: LoginModel, session: AsyncSession, response: Response):
    # check if email id exists 
    check_user_exists_query = select(Users).where(Users.email == data.email)
    result = await session.execute(check_user_exists_query)
    user = result.scalar_one_or_none()
    print ('user', user)
    if not user: 
         raise HTTPException(status_code=401, detail="invalid credentials")
    
    if not verify_password(data.password, user.password):
        raise HTTPException(status_code=400, detail="wrong credential")

    access_token = create_access_token(user.id)

    response.set_cookie(
        key="jwt_token",
        value=access_token,
        httponly=True,
        secure=True,      # HTTPS only
        samesite="lax"    # CSRF protection
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
