from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import EmailStr


class Users(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: EmailStr
    first_name: str
    last_name:str
    password: str

    
