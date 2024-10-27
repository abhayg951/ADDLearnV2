import strawberry
import typing
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from contextlib import asynccontextmanager
from .resolvers import get_user_data, create_user
from .schemas import User, ResponseUser, NewUser

# Connecting to the database while app startup
@asynccontextmanager
async def lifespan(app: FastAPI):
    print(" * Starting application..... * ")
    print(" * Connecting to the db server * ")
    yield # the application runs during this yield

    print(" * Closing database connection... * ")


@strawberry.type
class Query:
    user: typing.List[User] = strawberry.field(resolver=get_user_data)

@strawberry.type
class Mutation:
    @strawberry.mutation
    async def new_user(self, input: NewUser) -> ResponseUser:
        return await create_user(input)


schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql_app = GraphQLRouter(schema)

app = FastAPI(lifespan=lifespan)
app.include_router(graphql_app, prefix="/graphql")
