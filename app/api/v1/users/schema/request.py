from pydantic import BaseModel


class UserRegisterSchema(BaseModel):
    username: str
    password: str
    first_name: str | None = None
    last_name: str | None = None
    email: str | None = None