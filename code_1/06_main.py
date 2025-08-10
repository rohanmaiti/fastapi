#* Return type of any function 

from fastapi import FastAPI, Body;
from pydantic import BaseModel;
from typing import Annotated, Any;

app = FastAPI()



class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


@app.post("/items/")
async def create_item(item: Item) -> Item:
    return item

@app.get("/items/")
async def read_items() -> list[Item]:
    return [
        Item(name="Portal Gun", price=42.0),
        Item(name="Plumbus", price=32.0),
    ]

# response_model Parameter

@app.get('/items/', response_model=Item)
async def create_item(item: Item) -> Any:
    return Item

@app.post('/items/', respose_model=list[Item])
async def read_item(listOfItem: Annotated[ list[Item], Body()]= None) -> Any:
    return {
        "all_data": listOfItem
    }


# email validator 
# To use EmailStr, first install email-validator.
#  pip install email-validator
# or 
# $ pip install "pydantic[email]"

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None


# Don't do this in production!
@app.post("/user/")
async def create_user(user: UserIn) -> UserIn:
    return user


 # we should never return plain passowrd like this 
 # so we can make 2 models one for request and anther for response 

class Request(BaseModel):
    username: str
    email: EmailStr
    password: str
    
class Response(BaseModel):
    username:str
    email: EmailStr
    description: Any = None    

@app.post(
    '/post-route', response_model=Response
)
async def handlePost(data: [Annotated[Request, Body()]] = None) -> any:
    return {
        "username": data.username,
        "email": data.email,
        "description": {
            "name" : "rohan maiti",
            "age": "21"
        }
    }