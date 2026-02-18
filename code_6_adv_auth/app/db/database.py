# have to create a db engine to talk DB
# have to create a session to execute queries 

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from app.core.config import DATABASE_URL
from app.db.models import *

engine = create_async_engine(
    DATABASE_URL,
    echo = True
)

async_session = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

