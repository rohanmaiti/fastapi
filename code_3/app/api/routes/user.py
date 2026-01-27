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


# learning dependenci injection (db connections)
from fastapi import APIRouter, status, Depends
from app.schemas.user import UserCreate
from app.db.deps import get_db

router = APIRouter(
    prefix="/v1/users",
    tags=["Users"]
)

@router.post("/create-user", status_code=status.HTTP_201_CREATED)
async def create_user(
    user:UserCreate,
    db=Depends(get_db)
):
    print("user creating start")
    # res = await 
