import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession


@pytest.mark.asyncio
async def test_database_connection(db: AsyncSession):
    result = await db.execute(text("SELECT 1"))
    assert result.scalar() == 1

    