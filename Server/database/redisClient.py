import aioredis
from .config import REDIS_PORT, REDIS_HOST, REDIS_DB

class RedisClient:
    _redis = None  # 存储 Redis 连接实例

    @staticmethod
    async def get_client():
        """获取 Redis 连接实例"""
        if not RedisClient._redis:
            RedisClient._redis = await aioredis.from_url(
                f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}",
                decode_responses=True  # 让 Redis 以字符串格式返回数据
            )
        return RedisClient._redis

    @staticmethod
    async def set(key: str, value: str, expire: int = None):
        """设置键值对，可选设置过期时间"""
        client = await RedisClient.get_client()
        if expire:
            await client.setex(key, expire, value)
        else:
            await client.set(key, value)

    @staticmethod
    async def get(key: str):
        """获取键对应的值"""
        client = await RedisClient.get_client()
        return await client.get(key)

    @staticmethod
    async def delete(key: str):
        """删除键值对"""
        client = await RedisClient.get_client()
        await client.delete(key)

    @staticmethod
    async def exists(key: str) -> bool:
        """检查键是否存在"""
        client = await RedisClient.get_client()
        return await client.exists(key) == 1

    @staticmethod
    async def ping() -> bool:
        """检查 Redis 连接是否正常"""
        client = await RedisClient.get_client()
        try:
            return await client.ping()
        except aioredis.ConnectionError:
            return False

    @staticmethod
    async def close():
        """关闭 Redis 连接"""
        if RedisClient._redis:
            await RedisClient._redis.close()
            RedisClient._redis = None
