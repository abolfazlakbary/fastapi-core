from sqlalchemy import select, insert
from database.models import User
from core.authenticate.algorithms import hash_password
from core.database.connection import AsyncSession
from core.exceptions.exc import AuthFailedException, BadRequestException, ProccessFailedException



async def register(db: AsyncSession, username: str, password: str):
    stmt = (
        select(User)
        .where(User.username == username)
    )
    old_user = (await db.execute(stmt)).scalars().first()
    if old_user:
        raise BadRequestException("User with this username already exist")
    
    i_stmt = (
        insert(User)
        .values({"username": username, "hashed_password": hash_password(password)})
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
        .where(User.hashed_password == hash_password(password))
    )
    this_user = (await db.execute(stmt)).scalars().first()
    if not this_user:
        raise AuthFailedException()
    return this_user

