from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    phone_number: str

class UserRes(BaseModel):
    username: str
    email: EmailStr
    phone_number: Optional[str] | None = None

class UserOut(BaseModel):
    data: UserRes
    status: bool
    message: str
