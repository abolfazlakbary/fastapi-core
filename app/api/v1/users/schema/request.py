from pydantic import BaseModel


class UserRegisterSchema(BaseModel):
    username: str
    password: str
    email: str
    first_name: str | None = None
    last_name: str | None = None


class UserLoginSchema(BaseModel):
    username: str
    password: str