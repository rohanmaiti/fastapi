# from sqlmodel import select
# from sqlalchemy.ext.asyncio import AsyncSession
# from app.db.models import User


# async def create_user_repo(db: AsyncSession, user_data):
#     user = User(**user_data.dict())

#     db.add(user)
#     await db.commit()
#     await db.refresh(user)

#     return user


# async def get_all_users_repo(db: AsyncSession):
#     result = await db.execute(select(User))
#     return result.scalars().all()


from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models import User

async def create_user(db: AsyncSession, user_data): 
    user = User(**user_data.dict())
    