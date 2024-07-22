from pydantic import BaseModel
from core.database.connection import AsyncSession
from core.schema.validate import error_handler, check_email_is_valid



class UserRegisterSchema(BaseModel):
    username: str
    password: str
    email: str
    first_name: str | None = None
    last_name: str | None = None

    async def create_validation(self, db: AsyncSession, errors):
        if len(self.password) < 6:
            error_handler("Password too weak", "password", errors)
        
        if not check_email_is_valid(self.email):
            error_handler("Email is not correct", "email", errors) 
        return  errors


class UserLoginSchema(BaseModel):
    username: str
    password: str