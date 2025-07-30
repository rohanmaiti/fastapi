from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel
from typing import Annotated
from fastapi import Query


# creating a instance of FastAPI class to handle all http request 
app= FastAPI()

# simple get request 
@app.get('/home')
def home_page():
    return "Home page"

# path parameter | (dynamic route) params
# type - 1
@app.get('/item/{item_id}')
def getItem(item_id):
    # fetch the item from DB and return it 
    return {"item": item_id}

# can add type check in the above route 
@app.get('/getid/{id}')
def getId(id: int):
    return {"number_id": id}

# to get the path parameter as  predefined --> use Enum 
class UserID(str, Enum):
    aadhar =  "aadhar" 
    voter = "voter" 
    pan = "pan"

# in this api the user_id has to either of aadhar, voter or pan else will throw error 
@app.get('/user/{user_id}/{id_number}')
def getUserId(user_id: UserID, id_number:int):
    return {
        "id_type":user_id,
        "id_number": id_number
    }

# * Path convertor
# if you want to get a path as parameter like this 
# /app/file/{path_of_file}
# how you will write this ? and hit this as when you will hit this api 
# app/file/home/bin/bash -> then /home/bin/bash portion will be treated as route only insted of dynamic path
# sol --> use syntax like this 
@app.get('/app/file/{file_path:path}')
def getFilePath(file_path):
    return {
        "filePath": file_path
    }

# in the above case the route has to be -->http://127.0.0.1:8000/app/file//user/rohan/Desktop
# * note // after file and before user 


# * Query Parameters
# means when the url would be like this --> http://127.0.0.1:8000/?name={}&age={}
# here name and age are called query parameter
# to handle these kind of api 
@app.get('/users')
def userDetail(name: str, age: int | None = None ): # here age is optional 
    return {
        "username": name,
        "age": age
    }

# * Query Parameter + Path variable 
@app.get('/api/rollnumber/{id}')
def getRollNumber(id:int, name: str | None = None ):
    return {
        "rollNumber" : id,
        "username": name
    }


# * POST REQUESTS
from pydantic import BaseModel
class User(BaseModel):
    id: int
    name: str
    age: int | None = None # this means optional

@app.post('/add-user')
def addUser(user:User):
    return {
        "id": user.id,
        "name": user.name,
        "age": user.age,
        "university": "Chitkara University Himachal Pradesh"
    }

# POST REQUEST + query + path
@app.post('/api/v1/{university_id}')
def addUserInfo(university_id: int, user: User, college_name: str = "Chitkara University"):
    return {
        **dict(user),
        "university_id": university_id,
        "collegeName": college_name
    }

# FastAPI allows you to declare additional information and validation for your parameters.
# add validation max length to 50 in the q
# @app.get('get-q')
# def getQ(q: str | None = None):
#     return {
#         "Q" : q
#     }


@app.get("/get-q")
def getQ(q: Annotated[ str | None , Query(max_length=50)] = None):
    return {
        "Q": q
    }

@app.get('/learn-query')
def learnQuery(q: Annotated[str | None, Query(max_length=10, title="Learning Query Anotation", description="this value is a")] = None):
    print(q)
    return {
        "Q" : q
    }