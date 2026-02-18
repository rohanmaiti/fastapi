from app.api.auth.schemas.request import *
from app.db.models import *


class AuthService():
    async def handle_signup(data: SignupModel):
        return 400
        # check user in db
        
        # add user in db

        # create access token + refresh token 

        # send this to client 

    async def handle_login(data: LoignModel):
        return 400
        # check user if db 

        # create tokens 

        # send token

    async def handle_refersh(): 
        return
        # get token
        
        # validate token 

        # genrate token and sent new token
