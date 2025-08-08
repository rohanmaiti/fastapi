from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Annotated
app = FastAPI()

# so till now have learned how we handle request body -->
# but what if the req body is like this --> ??
"""
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    }
}
"""

# no problem it will handle it as it was handling it previously --> you have to make two class item and user
# that's it -- rest  python will handle it automatically 

class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float = 0

class User(BaseModel):
    username: str
    fullName: str

@app.post('/post-nested-body')
async def handleNestedBody( item: Item, user:User ):
    return {
        **dict(item),
        **dict(user)
    }

# if you have single key to send through body with the above example like this 
"""
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    },
    "importance": 5
}
"""
# then writing this --> async def handleNestedBody( item: Item, user:User, importance: int )
# here importance will be treated as PQuery Parameter
# you have to explecitely mention it as a body paremeter like this --> 
@app.post('/post-nested-body/single-value')
def handle_function(item: Item, user: User, importance: Annotated[int, Body()]):
    return {
        **dict(item),
        **dict(user),
        "importance" : importance
    }


# Now what have you undersand till now ??
"""
if you want to send a body like this --> 

    {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    }

then you would be using syntax like this 
@app.get()
def function(item: Item) 
and you will write the Item class but what if you want it like this ??
{
"item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    }
}

then youe have to mention embaded inside body

"""



@app.post('/learn-embed')
def handleEmbaded(item: Annotated[Item, Body(embed=True)]):
    return {
        **dict(item)
    }