from fastapi import APIRouter, Depends
from app.schemas.users.auth_schemas import UserIn, UserOut, SignUpResponse
from app.services.users.users import User
from app.db.dependencies import get_db

router = APIRouter(prefix="/v1/user")

# user-signlup
@router.post("/signup", response_model=SignUpResponse)
async def signup(data: UserIn, db=Depends(get_db)) -> SignUpResponse: # here the SignupResponse does not validate in run time, it just check types in compile time 
    user_data = data.model_dump()
    user = User(user_data)
    # user.print_data()
    res = await user.insert_into_db(db)
    print("res", res)

    return {
        "message": "signup route",
        "status": 200,        
        "data": user.data,
        "abc": "123" # if there is something more that response field then fast api filterd out them by default --> No error
                     # But if there is something that is missing from the res-model then it will give 500 error
    }


@router.get("/get-all-user")
async def get_all_user(db=Depends(get_db)):
    return await User.get_all_users(db)



# @router.post("/login")
# async def login


"""
why to do `data.model_dump()`
as the data that is comming through the request body is not dict but a pydantic model object 
so that's why you can not perform operation of dict on this so to covert it into dict we use model_dump() function.
"""

