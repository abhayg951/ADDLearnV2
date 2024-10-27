from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient("mongodb://localhost:27017/")  # connecting to the mongodb server
db = client.get_database("AddLearnV2_Authentication")  # creating the database
user_collection = db.get_collection("Users")  # creating the user collection