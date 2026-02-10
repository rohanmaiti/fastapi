from fastapi import FastAPI
from app.api.auth import router
from fastapi.middleware.cors import CORSMiddleware
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


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router, prefix="/api")

