from sqlalchemy import select, insert, or_
from database.models import User
from core.authenticate.algorithms import hash_password, create_access_token
from core.database.connection import AsyncSession
from core.exceptions.exc import AuthFailedException, BadRequestException, ProccessFailedException
from datetime import timedelta
from core.config.data import configs
from core.authenticate.settings import pwd_context



async def register(db: AsyncSession, form_data):
    request_data = form_data.model_dump(exclude=["password"])
    stmt = (
        select(User)
        .where(
            or_(
                User.email == request_data.get("email"),
                User.username == request_data.get("username")
            )
        )
    )
    old_user = (await db.execute(stmt)).scalars().first()
    if old_user:
        raise BadRequestException("User with this data already exist")
    i_stmt = (
        insert(User)
        .values(
            {
                **request_data,
                "hashed_password": hash_password(form_data.password)
            }
        )
        .returning(User)
    )
    new_user = (await db.execute(i_stmt)).scalars().first()
    await db.commit()
    
    if not new_user:
        raise ProccessFailedException("Register unsuccessfull")
    
    return new_user



async def login_user(db: AsyncSession,username: str, password: str):
    stmt = (
        select(User)
        .where(User.username == username)
    )
    this_user = (await db.execute(stmt)).scalars().first()
    if not this_user or not pwd_context.verify(password, this_user.hashed_password):
        raise AuthFailedException()
    
    access_token_expires = timedelta(minutes=configs.access_token_expire_minutes)
    access_token = create_access_token(
        data={
            "sub": {
                "username": username
            }
        },
        expires_delta=access_token_expires
    )
    
    return access_token

