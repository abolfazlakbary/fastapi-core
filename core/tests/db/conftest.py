import pytest_asyncio
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from core.database.connection import db_uri


@pytest_asyncio.fixture()
async def db():
    engine = create_async_engine(db_uri)
    async_session_factory = async_sessionmaker(
        engine, expire_on_commit=False
    )

    async with async_session_factory() as session:
        try:
            yield session
        except:
            raise SystemError("Session Interaction failed")
        finally:
            await session.close()
            await engine.dispose()