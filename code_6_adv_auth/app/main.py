from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db.database import init_db
from app.api.router import router as central_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("starting server ...")
    await init_db()
    print("db connected ...")    
    print("start developing")
    yield
    print("shutting down server...")

app = FastAPI(lifespan=lifespan)

app.include_router(central_router)

@app.get('/')
async def root():
    return {
        "message": "Welcome to the website"
    }


