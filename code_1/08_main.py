# 
#* Response status code
from fastapi import FastAPI;
app = FastAPI()

app.post('/getuser', status_code=200) # this is default status code
def handleGetUser(user: str):
    return {
        "username": user
    }