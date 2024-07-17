from core.config.data import configs
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base
import os


Base = declarative_base()


match configs.db_connection:
    case "sqlite":
        absolute_directory = os.path.dirname(os.path.abspath(__file__))
        file_directory = "file"
        db_directory = os.path.join(absolute_directory, file_directory)
        db_file_name = "database.db"
    
        if not os.path.exists(db_directory):
            os.makedirs(db_directory)
            
        file_path = os.path.join(db_directory, db_file_name)
        with open(file_path, 'w') as db_file:
            pass
        engine = create_async_engine(f'sqlite+aiosqlite:///{file_path}')
    
    case "mysql":
        pass
    
    case "postgres":
        pass
    
    case _:
        raise ValueError("Database connection failed")


async_session = AsyncSession(engine, expire_on_commit=False)


async def init_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
