from pydantic import BaseModel
from typing import Optional

class UserIn(BaseModel):
    email: str
    first_name: str
    last_name: Optional[str] = None
    password: str

class UserOut(BaseModel):
    email: str
    first_name: str
    last_name: Optional[str]

class SignUpResponse(BaseModel):
    message: str
    status: int
    data: UserOut

class  UserLogin(BaseModel):
    email: str
    password: str        

class LoginResponse(SignUpResponse):
    token: str
    

