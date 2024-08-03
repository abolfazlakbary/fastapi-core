import redis.asyncio as redis
from core.config.data import configs
import pytest
import asyncio


@pytest.mark.asyncio
async def test_redis_connection():
    client = redis.Redis(host=configs.redis_host, port=configs.redis_port, db=configs.redis_db_number)
    try:
        await asyncio.wait_for(client.ping(), timeout=5)
    except Exception as e:
        raise SystemError(f"Connection to Redis Unsuccessful, {e}")
    finally:
        await client.aclose()