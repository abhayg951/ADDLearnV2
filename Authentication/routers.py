from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from .schema import NewUser, UserResponse
from .utils import MongoClient
from motor.motor_asyncio import AsyncIOMotorDatabase
from dotenv import load_dotenv
import os

load_dotenv()

# router
router = APIRouter()

# db Configuration
client = MongoClient(os.getenv("MONGO_URI"), AsyncIOMotorDatabase)
client.mongo_connection()
collection = client.db.get_collection("Users")

@router.post("/register", response_model=UserResponse)
async def register(user_body: NewUser):
    find_user = await collection.find_one({"email": user_body.email})
    if find_user:
        print("user already registered")
        raise HTTPException(detail="User with already exists", status_code=status.HTTP_400_BAD_REQUEST)
    inserted_user = await collection.insert_one(user_body.model_dump())
    new_user = await collection.find_one({"_id": inserted_user.inserted_id})
    return new_user