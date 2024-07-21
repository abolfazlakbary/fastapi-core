from fastapi import APIRouter, Security, Depends
from core.database.connection import db_session
from .controller import UserController
from core.authenticate.auth import register
from typing import Annotated
from .schema.request import UserRegisterSchema


controller = UserController()


user_router = APIRouter(tags=["Users"], prefix="/users")


@user_router.get(
    "/all"
)
async def get_all_users(db: db_session):
    data = await controller.query_all_users(db)
    return data


@user_router.get(
    "/{u_id}/get"
)
async def get_user_by_id(
    db: db_session,
    u_id: int
):
    data = await controller.query_get_user_by_id(db, u_id)
    return data



@user_router.post(
    "/register"
)
async def register_new_user(
    db: db_session,
    form_data: UserRegisterSchema
):
    new_user = await register(db, form_data)
    return new_user