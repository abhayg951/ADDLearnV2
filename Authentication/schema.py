from pydantic import BaseModel, Field
from bson import ObjectId
from .utils import PyObjectId
from datetime import datetime

class Token(BaseModel):
    access_token: str
    token_type: str

class UserResponse(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    email: str
    role: str = "student"
    phone_number: str | None
    profile_img: str | None
    bio: str | None
    address: str | None
    created_at: datetime

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class NewUser(BaseModel):
    name: str = ...
    email: str = ...
    password: str = ...
    role: str = "student"
    profile_img: str = None
    bio: str = None
    address: str = None
    phone_number: str = None
    created_at: datetime = datetime.now()