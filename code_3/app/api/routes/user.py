# from fastapi import APIRouter, status
# from app.schemas.user import UserCreate, UserOut

# router = APIRouter(prefix="/users", tags=["Users"])

# @router.post('/create-user', status_code=status.HTTP_201_CREATED, response_model=UserOut)
# async def create_user(user: UserCreate):
#     print(f"user creating")
#     print(f"creating user of username = {user.username}")
#     return {
#        "data": {
#            "username": user.username,
#             "email": user.email
#        },
#        "status": True,
#        "message": "user created successfully"
#     }


from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.user import UserCreate, UserResponse
from app.db.deps import get_db
from app.services.user_service import create_user_service, get_users_service

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/", response_model=UserResponse)
async def create_user_api(
    user: UserCreate,
    db: AsyncSession = Depends(get_db)
):
    return await create_user_service(db, user)


@router.get("/", response_model=list[UserResponse])
async def get_users_api(
    db: AsyncSession = Depends(get_db)
):
    return await get_users_service(db)

