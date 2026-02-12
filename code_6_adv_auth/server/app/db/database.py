from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from app.core.config import DATABASE_URL, ENVIRONMENT

engine=create_async_engine(
    DATABASE_URL,
    echo=(ENVIRONMENT == "development")
)

async_session = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def init_db():
    from app.db import models
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

        
