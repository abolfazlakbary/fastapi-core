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
        
        db_uri = f'sqlite+aiosqlite:///{file_path}'
        engine = create_async_engine(db_uri)
    
    case "postgres":
        db_uri = f'postgresql+asyncpg://{configs.db_username}:{configs.db_password}@{configs.db_host}:{configs.db_port}/{configs.db_name}'
        engine = create_async_engine(db_uri)
    
    case "mysql":
        db_uri = f'mysql+aiomysql://{configs.db_username}:{configs.db_password}@{configs.db_host}:{configs.db_port}/{configs.db_name}'
        engine = create_async_engine(db_uri)

    case _:
        raise ValueError("Database connection failed")


async_session = AsyncSession(engine, expire_on_commit=False)


async def init_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
