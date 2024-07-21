import redis.asyncio as redis
from core.config.data import configs

async def redis_connection():
    client = redis.Redis(host=configs.redis_host, port=configs.redis_port, db=configs.redis_db_number)
    try:
        await client.ping()
        await client.aclose()
    except:
        raise SystemError("Connection to Redis Unsuccessfull")