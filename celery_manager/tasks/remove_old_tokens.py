from celery_manager.celery_app import celery_app
from core.redis.connection import redis_connection
import asyncio


async def _remove_data():
    redis_client = await redis_connection()
    async for key in redis_client.scan_iter():
        await redis_client.delete(key)
        
@celery_app.task(name="remove-data")
def remove_data():
    asyncio.run(_remove_data())