from sqlmodel import SQLModel, Field
from typing import Optional


class Users(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str
    password: int
    first_name: str
    last_name: Optional[str] = None
    