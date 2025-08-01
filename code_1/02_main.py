from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Annotated
from pydantic import AfterValidator
from typing import Annotated


#* HANDLING POST REQUEST 
app = FastAPI()

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
        **dict(user), # here ** means spread operator 
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

# without annotated 
@app.get('/get-q')
def getQ(q: str | None = None):
    return {
        "Q": q
    }


# with Annotated --> what is the advantage then ??
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


# * More on  Query 
# q: Annotated[str, Query(default="rick")] = "morty"
# you cant write like this as this creates confusion....

# * we can right multiple check inside Query()
@app.get("/learn-query-v2")
async def funcname(q: Annotated[str | None, Query(max_length=10, default_value='abc')]):
    return {
        "Q" : q
    }

# we can add custom validations as well using #* AfterValidator
data = {
    "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
    "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
    "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
}

class Id(BaseModel):
    id: str | None = None

def custom_check(id: Id):
    id_str = id.id
    if not id_str.startswith(('imdb', 'isbn')):
        raise ValueError("Invalid Id Format")
    return id

@app.post('/custom-check')
def custom_check(id: Annotated[Id | None, AfterValidator(custom_check)  ]=None):
    if not id:
        return ({"hello": "Hello user, hitting POST at /custom-check"})
    else :
        return ({
            "hello": "Hello user, hitting POST at /custom-check",
            "id": id.id
        })
