from pydantic import BaseModel, EmailStr
from typing import Optional



class SingupModel(BaseModel):
    email: EmailStr
    first_name: str
    last_name: Optional[str] = None
    password: str


class LoginModel(BaseModel):
    email: EmailStr
    password: str

    