from tortoise import Tortoise
from .config import DATABASE_CONFIG

class Database:
    @staticmethod
    async def init():
        """建立数据库连接"""
        await Tortoise.init(config=DATABASE_CONFIG)
        await Tortoise.generate_schemas()

    @staticmethod
    async def close():
        """关闭数据库连接"""
        await Tortoise.close_connections()

