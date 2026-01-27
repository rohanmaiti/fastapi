from pydantic import BaseModel, EmailStr
from typing import Optional

class ProductCreate(BaseModel):
    product_id: str
    name: str
    quantity: int
    user_id: str    

class ProductCreate(BaseModel):
    status: bool
    created_at: str
    product_id: str


    