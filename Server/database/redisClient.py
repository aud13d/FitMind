import aioredis
from .config import REDIS_PORT, REDIS_HOST, REDIS_DB

class RedisClient:
    _redis = None  # 存储 Redis 连接实例

    @staticmethod
    async def get_client():
        if not RedisClient._redis:
            RedisClient._redis = await aioredis.from_url(
                f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}",
                decode_responses=True  # 让 Redis 以字符串格式返回数据
            )
        return RedisClient._redis

    @staticmethod
    async def set(key: str, value: str, expire: int = None):
        client = await RedisClient.get_client()
        if expire:
            await client.setex(key, expire, value)
        else:
            await client.set(key, value)

    @staticmethod
    async def get(key: str):
        client = await RedisClient.get_client()
        return await client.get(key)

    @staticmethod
    async def delete(key: str):
        client = await RedisClient.get_client()
        await client.delete(key)

    @staticmethod
    async def exists(key: str) -> bool:
        client = await RedisClient.get_client()
        return await client.exists(key) == 1

    @staticmethod
    async def ping() -> bool:
        client = await RedisClient.get_client()
        try:
            return await client.ping()
        except aioredis.ConnectionError:
            return False

    @staticmethod
    async def close():
        if RedisClient._redis:
            await RedisClient._redis.close()
            RedisClient._redis = None
