from app.core.config import HASHING_SECRET
from app.db.models import Users as User_model
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

class User:
    def __init__(self, data):
        self.user = data
        self.__hash_password()

    def print_data(self):
        print("Printing user data")
        print(self.user)

    def __hash_password(self):
        password = self.user["password"]
        hashed_password = password + str(HASHING_SECRET)
        self.user["password"] = hashed_password

    # getter
    @property
    def data(self):
            user = self.user.copy()
            del user["password"]
            return user
    
    async def insert_into_db(self, db: AsyncSession):
         print("inserting user info into db")
         user = User_model(**(self.user))
         db.add(user)
         await db.commit()
         res = await db.refresh(user)
         print("printing res", res)
         return res
    
    @staticmethod
    async def get_all_users(db: AsyncSession):
        result = await db.execute(select(User_model))
        return result.scalars().all()
