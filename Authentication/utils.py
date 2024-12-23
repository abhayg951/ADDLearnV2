from motor.motor_asyncio import AsyncIOMotorDatabase, AsyncIOMotorClient
from bson import ObjectId
from pydantic import BaseModel, Field
from typing import Any

# MongoDB Class
class MongoClient():
    def __init__(self, mongo_uri: str, db: AsyncIOMotorDatabase):
        self.mongo_uri = mongo_uri
        self.db = db

    def mongo_connection(self):
        client = AsyncIOMotorClient(self.mongo_uri)
        self.db = client.get_database("AddLearnV2_Authentication")

# Custom Pydantic Type for ObjectId
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate
    
    @classmethod
    def validate(cls, v: Any, field=None):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)
    
    @classmethod
    def __get_pydantic_json_schema__(cls, field_schema):
        field_schema.update(type="string")