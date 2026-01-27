from app.core.config import DATABASE_URL
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel

engine = create_async_engine(
    DATABASE_URL,
    echo=True,   # shows SQL logs (disable in prod)
    future=True
)

async_session = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)


async def init_db():
    from app.db import models   # IMPORTANT: prevents circular import
    
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
