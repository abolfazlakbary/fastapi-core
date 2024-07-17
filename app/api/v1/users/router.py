from fastapi import APIRouter
from core.database.connection import db_session
from .controller import UserController


controller = UserController()


user_router = APIRouter(tags=["Users"], prefix="/users")


@user_router.get(
    "/all"
)
async def get_all_users(db: db_session):
    data = await controller.query_all_users(db)
    return data