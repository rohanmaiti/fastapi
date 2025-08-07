#** COOKIE PARAMETER
from typing import Annotated;
from fastapi import FastAPI, Cookie, Header
from pydantic import BaseModel


app = FastAPI()

@app.post('/getting-cookie')
def handle_cookie(item: Annotated[str, Cookie()] = None):
    return {
        "cookie": item
    }




# # ** Header() 
# @app.post('/get-header-content')
# def getHeader(x_auth: Annotated[ str | None, Header() ]=None):
#     return {
#         "Printing header": x_auth
#     }

# It is possible to receive duplicate headers. That means, the same header with multiple values.
# You will receive all the values from the duplicate header as a Python list
@app.post('/get-header-content')
def getHeader(x_auth: Annotated[ list[str] | None, Header() ]=None):
    return {
        "Printing header": x_auth
    }



# cookie model 

# class Cookies(BaseModel):
#     session_id: str
#     fatebook_tracker: str | None = None
#     googall_tracker: str | None = None


# @app.get("/items/")
# async def read_items(cookies: Annotated[Cookies, Cookie()]):
#     return cookies

# header model
class CommonHeaders(BaseModel):
    host: str
    save_data: bool
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = []


@app.get("/items/")
async def read_items(headers: Annotated[CommonHeaders, Header()]):
    return headers


