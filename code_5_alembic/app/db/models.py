from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from pydantic import EmailStr
import uuid

class Users(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    email: EmailStr
    first_name: str
    last_name: Optional[str]
    password: str

class Blog(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    title: str
    content: str
    author_id: str = Field(foreign_key="users.id")
    blog_img_url: Optional[str] = None
    # Optional: relationship to access the author
    # author: Optional[Users] = Relationship(back_populates="blogs") 

    