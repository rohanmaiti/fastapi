# from fastapi import FastAPI
# from fastapi import Query

# or can write like this as well 
from fastapi import FastAPI, Query

# importing enum 
from enum import Enum





# *creating a instance of FastAPI class to handle all http request 
app= FastAPI()

#* simple get request 
@app.get('/home')
def home_page():
    return "Home page"

# path parameter | (dynamic route) params
# type - 1
@app.get('/item/{item_id}')
def getItem(item_id):
    # fetch the item from DB and return it 
    return {"item": item_id}

# type - 2
# can add type check in the above route by defining type of query parameter
@app.get('/getid/{id}')
def getId(id: int): 
    return {"number_id": id}

# type - 3
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

# type - 4
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

