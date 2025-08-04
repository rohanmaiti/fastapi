#** COOKIE PARAMETER
from typing import Annotated;
from fastapi import FastAPI, Cookie

app = FastAPI()

@app.get('/getting-cookie')
def handle_cookie(item: Annotated[str, Cookie()]):
    return {
        "cookie": item
    }