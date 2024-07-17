from app.fastapi_app import app
from core.database.connection import init_database
from database import models


async def run_server():
    await init_database()
