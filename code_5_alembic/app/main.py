from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db.database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("starting server..")
    await init_db()
    print("db connected")
    yield 
    print("shutting down")


app = FastAPI(lifespan=lifespan)



