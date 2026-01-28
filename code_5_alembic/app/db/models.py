from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import EmailStr
import uuid

class Users(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    email: EmailStr
    first_name: str
    last_name: Optional[str]
    password: str