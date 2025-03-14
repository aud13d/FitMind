from ..models.user import User
from ..database.redisClient import RedisClient
from .config import CODE_EXPIRATION
class DataService:
    @staticmethod
    async def check_email_exists(email: str):
        # 查询数据库，检查邮箱是否已经存在
        existing_email = await User.filter(email=email).first()
        return existing_email is not None

    @staticmethod
    async def check_username_exists(username: str):
        # 查询数据库，检查用户名是否已经存在
        existing_username = await User.filter(username=username).first()
        return existing_username is not None

    @staticmethod
    async def verify_user_password(username: str, password: str):
        # 验证用户密码是否匹配
        return await User.verify_password(username, password)

    @staticmethod
    async def get_user_by_email(email: str):
        # 获取用户信息
        return await User.filter(email=email).first()

    @staticmethod
    async def update_user_password(email: str, password: str):
        # 更新用户密码
        return await User.update_password(email, password)

    @staticmethod
    async def create_new_user(email: str, username: str, password: str):
        # 创建新用户
        await User.create_user(email, username, password)

    # Redis 操作
    @staticmethod
    async def get_verification_code_from_redis(email: str):
        # 从 Redis 获取存储的验证码
        return await RedisClient.get(email)

    @staticmethod
    async def delete_verification_code_from_redis(email: str):
        # 删除 Redis 中的验证码
        await RedisClient.delete(email)

    @staticmethod
    async def set_verification_code_to_redis(email: str, code: str, expire: int = CODE_EXPIRATION):
        # 将验证码存入 Redis，并设置过期时间
        await RedisClient.set(email, code, expire=expire)
