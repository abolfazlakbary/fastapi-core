from pydantic import BaseModel
from core.database.connection import AsyncSession
from core.schema.validate import error_handler


class UserRegisterSchema(BaseModel):
    username: str
    password: str
    email: str
    first_name: str | None = None
    last_name: str | None = None

    async def create_validation(self, db: AsyncSession, errors):
        return  errors


class UserLoginSchema(BaseModel):
    username: str
    password: str