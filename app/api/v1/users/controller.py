from sqlalchemy import select
from core.database.connection import AsyncSession
from database.models import User
from core.exceptions.exc import NotFoundException


class UserController:

    @staticmethod
    async def query_all_users(db: AsyncSession):
        stmt = (
            select(User)
        )
        users = (await db.execute(stmt)).scalars().all()
        if not users:
            raise NotFoundException("No users found")
        return users


    @staticmethod
    async def query_get_user_by_id(db: AsyncSession, u_id: int):
        stmt = (
            select(User)
            .where(User.id == u_id)
        )
        this_user = (await db.execute(stmt)).scalars().first()
        if not this_user:
            raise NotFoundException("User does not exist")
        return this_user
