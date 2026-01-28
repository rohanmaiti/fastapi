from fastapi import FastAPI
from app.api.routes.users import router as user_router
from contextlib import asynccontextmanager
from app.db.database import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("starting app")
    print("connecting to db....")
    await init_db()
    print("db connected")
    yield
    print("Shutting down app")


app = FastAPI(lifespan=lifespan)

app.include_router(user_router, prefix="/api")