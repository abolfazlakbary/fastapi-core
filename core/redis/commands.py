from core.redis.connection import redis_connection

async def add_token_to_blacklist(token: str):
    client = await redis_connection()
    await client.sadd("token_blacklist", token)


async def check_token_is_in_blacklist(token: str):
    client = await redis_connection()
    token_in_blacklist = await client.sismember("token_blacklist", token)
    if token_in_blacklist:
        return True
    return False
