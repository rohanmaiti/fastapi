from fastapi import FastAPI, status
from pydantic import BaseModel, EmailStr
from typing import Optional

app = FastAPI()

@app.get('/')
def root():
    return {"message": "FastAPI is running.."}

@app.get('/health')
def health():
    return {"Status": "Ok"}

class UserCreate(BaseModel): 
    name: str
    email: EmailStr
    age: int
    phone: Optional[str] = None


class UserResponse(BaseModel):
    success: bool
    data: UserCreate
    message: str   

@app.post('/create-user', status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def create_user(user: UserCreate):
    return {
        "success": True,
        "data": user,
        "message": "User created"
    }

@app.get("/info")
async def info():
    return {
        "app": "FastAPI Learning.."
    }
@app.post("/login-test", status_code=status.HTTP_200_OK)
async def login_test():
    return {
        "message": "Login API hit"
    }

class ProductCreate(BaseModel): 
    name: str
    price: float
    in_stock: bool

@app.post('/create-product', status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductCreate):
    return {
        "message": "Product created",
        "product": product
    }

