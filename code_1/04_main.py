# nested-models
from fastapi import FastAPI, Body
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()


"""
lets make the req.body like this -->
{
    user_details: {
        "user_info": {
            "username": "rohanmaiti",
            "fullname": "Rohan Maiti"
         },
        "bank_detials": {
            "account_no": "1234556766",
            "branch_details": {
                "branch_name" : "sabang",
                "IFSE_code": "SBN1234"
             }
         }
    }
}

how the class of it should look like ?
>> you have to make from deep nested to uper level
"""


class Branch_details(BaseModel):
    branch_name: str
    IFSE_code: str = "SBN1234"

class Bank_detials(BaseModel):
    account_no: str
    branch_details : Branch_details

class UserInfo(BaseModel):
    username: str
    fullname: str

class User_details(BaseModel):
    user_info: UserInfo
    bank_details: Bank_detials

@app.post('/nested-data')
def func(data:  Annotated[User_details, Body(embed=True)] = None):

    if data is not None:
        return {
            **dict(data),
            "status" : "success"
        }
    else:
        return {
            "status": "not-success"
        }

