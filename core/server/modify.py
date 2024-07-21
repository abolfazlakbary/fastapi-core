from app.fastapi_app import app
from core.database.connection import init_database
from database import models
from core.redis.connection import redis_connection


async def run_server():
    await init_database()
    await redis_connection()
