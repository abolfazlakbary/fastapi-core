from fastapi import APIRouter, Security
from core.database.connection import db_session
from .controller import UserController
from core.authenticate.auth import register, login_user, check_authentication
from .schema.request import UserRegisterSchema, UserLoginSchema
from core.authenticate.schema.response import CurrentUserResponseShema
from core.redis.commands import add_token_to_blacklist
from core.exceptions.exc import AuthFailedException



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
async def get_personal_info(current_user = Security(check_authentication)):
    return current_user.get("data")



@user_router.get("/logout")
async def user_logout(current_user = Security(check_authentication)):
    token = current_user.get("token")
    if not token:
        raise AuthFailedException("You are not logged in")
    await add_token_to_blacklist(token)
    return {"message": "successfully logged out"}