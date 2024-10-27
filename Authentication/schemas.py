import strawberry
import datetime
from bson import ObjectId

# for fetching user
@strawberry.type
class User:
    # id: uuid.UUID
    name: str
    role: str = "student"
    email: str

# for creating user
@strawberry.input
class NewUser:
    name: str
    role: str = "student"
    email: str
    username: str
    phone_number: str
    password: str
    confirm_password: str
    profile_picture: str
    bio: str
    address: str
    created_at: datetime.datetime = datetime.datetime.now()

@strawberry.type
class ResponseUser:
    _id: strawberry.ID
    name: str
    role: str = "student"
    email: str
    username: str
    phone_number: str
    password: str
    confirm_password: str
    profile_picture: str
    bio: str
    address: str
    created_at: datetime.datetime = datetime.datetime.now()