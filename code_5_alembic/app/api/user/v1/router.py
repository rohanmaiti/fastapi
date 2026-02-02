
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from .request import SingupModel, LoginModel
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.dependency import get_db
from app.api.user.v1.services.auth import does_user_exists, insert_user_in_db, handle_login


router = APIRouter(prefix="/v1/user", tags=["Users"])

content={"status": "healthy", "service": "api helath checkup"}

@router.get("/health")
def root_router():
    response = JSONResponse(
        status_code=200,
        content=content
    )
    response.set_cookie(key="X-custom", value="admin123")
    return response 

 

@router.post("/signup")
async def signup(data: SingupModel, session: AsyncSession=Depends(get_db)):
    if (await does_user_exists(data, session)):
        return JSONResponse(
            status_code=400,
            content={"message": "user already exists"}
        )
    # else creating new user in the db
    res = await insert_user_in_db(data, session)
    return res


@router.post("/login")
async def login(data: LoginModel, session: AsyncSession = Depends(get_db)):
    handle_login(data, session)


    
