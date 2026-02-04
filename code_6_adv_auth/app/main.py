from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db.database import init_database

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("starting app...")
    await init_database()
    print("db connected...")
    yield 
    print("shuttingdown app...")    



app = FastAPI(lifespan=lifespan)
