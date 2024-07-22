from fastapi import APIRouter
from core.database.connection import db_session
from .controller import UserController
from core.authenticate.auth import register, login_user, token_data
from .schema.request import UserRegisterSchema, UserLoginSchema
from core.authenticate.schema.response import CurrentUserResponseShema


controller = UserController()
user_router = APIRouter(tags=["Users"], prefix="/users")


@user_router.post(
    "/register"
)
async def register_new_user(
    db: db_session,
    form_data: UserRegisterSchema
):
    new_user = await register(db, form_data)
    return new_user


@user_router.post("/login")
async def login_for_access_token(
    db: db_session,
    form_data: UserLoginSchema
):
    data = await login_user(db, form_data.username, form_data.password)
    return data



@user_router.get(
    "/me",
    response_model=CurrentUserResponseShema
)
async def get_personal_info(current_user = token_data):
    return current_user.get("data")