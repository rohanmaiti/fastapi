from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from pydantic import EmailStr
from datetime import datetime, timezone
import uuid

class Users(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    email: EmailStr = Field(unique=True, index=True)
    first_name: str
    last_name: Optional[str] = None
    password: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class Blog(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    title: str
    content: str
    author_id: str = Field(foreign_key="users.id")
    blog_img_url: Optional[str] = None
    # Optional: relationship to access the author
    # author: Optional[Users] = Relationship(back_populates="blogs") 

    