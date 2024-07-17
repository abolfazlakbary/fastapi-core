from sqlalchemy import select
from core.database.connection import AsyncSession
from database.models import User


class UserController:

    @staticmethod
    async def query_all_users(db: AsyncSession):
        stmt = (
            select(User)
        )
        users = (await db.execute(stmt)).scalars().all()
        return users

