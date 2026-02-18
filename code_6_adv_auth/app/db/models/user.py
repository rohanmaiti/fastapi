from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from .todo import *

class User(SQLModel, table=True):
    __tablename__ = 'users'
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str = Field(index=True, unique=True)
    password: str
    posts: List["Todo"] = Relationship(back_populates="user")

