#** COOKIE PARAMETER
from typing import Annotated;
from fastapi import FastAPI, Cookie

app = FastAPI()

@app.post('/getting-cookie')
def handle_cookie(item: Annotated[str, Cookie()] = None):
    return {
        "cookie": item
    }