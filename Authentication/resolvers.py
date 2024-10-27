import typing
from . import schemas
from .utils import user_collection
import strawberry

# resolver function
def get_user_data(root) -> typing.List[schemas.User]:
    pass

async def create_user(body: schemas.NewUser) -> schemas.ResponseUser:
        print(f"adding user {body}")
        new_user = await user_collection.insert_one(strawberry.asdict(body))
        print("Done")
        user = await user_collection.find_one({"_id": new_user.inserted_id})
        print(user)
        return schemas.ResponseUser(**user)