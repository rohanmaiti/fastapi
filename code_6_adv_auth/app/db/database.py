from app.core.config import DATABASE_URL
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel


engine = create_async_engine(
    DATABASE_URL,
    echo=False,
    future=True
)

async_session = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def init_database():
    from app.db import models
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)