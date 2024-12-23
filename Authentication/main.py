from fastapi import FastAPI
from contextlib import asynccontextmanager
from motor.motor_asyncio import AsyncIOMotorDatabase
from .utils import MongoClient
from .routers import router as auth_router 

mongodb = MongoClient("mongodb://localhost:27017", AsyncIOMotorDatabase)

@asynccontextmanager
async def lifespan(app: FastAPI):
    print(" * Starting application * ")
    print(" * Connecting to DB * ")
    mongodb.mongo_connection()
    yield
    print(" * Stopping application * ")

app = FastAPI(lifespan=lifespan)

@app.get("/")
def home():
    return {"message": "Welcome to AddLearn"}

app.include_router(auth_router, prefix="/auth")