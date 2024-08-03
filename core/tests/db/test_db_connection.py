import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
import asyncio


@pytest.mark.asyncio
async def test_database_connection(db: AsyncSession):
    try:
        result = await asyncio.wait_for(
                db.execute(text("SELECT 1")), timeout=5
            )
        assert result.scalar() == 1
    except Exception as e:
        raise SystemError(f"Connection to database failed. {e}")
    