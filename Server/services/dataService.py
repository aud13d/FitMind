from typing import List, Literal

from ..models.aerobic import Aerobic
from ..models.user import User
from ..database.redisClient import RedisClient
from .config import CODE_EXPIRATION
from ..models.userSportsInfo import UserSportsInfo
from ..models.train import Train

class DataService:
    @staticmethod
    async def check_email_exists(email: str):
        """检查邮箱是否已经存在"""
        existing_email = await User.filter(email=email).first()
        return existing_email is not None

    @staticmethod
    async def check_username_exists(username: str):
        """检查用户名是否已经存在"""
        existing_username = await User.filter(username=username).first()
        return existing_username is not None

    @staticmethod
    async def verify_user_password(username: str, password: str):
        """验证用户密码是否匹配"""
        return await User.verify_password(username, password)

    @staticmethod
    async def get_user_by_email(email: str):
        """根据邮箱获取用户信息"""
        return await User.filter(email=email).first()

    @staticmethod
    async def update_user_password(email: str, password: str):
        """更新用户密码"""
        return await User.update_password(email, password)

    @staticmethod
    async def create_new_user(email: str, username: str, password: str):
        """创建新用户"""
        await User.create_user(email, username, password)

    @staticmethod
    async def get_user_id(username: str):
        """获取用户ID"""
        return await User.get_user_id(username)

    @staticmethod
    async def set_user_logged_in(username:str):
        """设置用户登录状态"""
        await User.set_logged_in(username)

    @staticmethod
    async def set_user_logged_out(username:str):
        """设置用户登出状态"""
        await User.set_logged_out(username)

    # Redis 操作
    @staticmethod
    async def get_verification_code_from_redis(email: str):
        """从Redis中获取验证码"""
        return await RedisClient.get(email)

    @staticmethod
    async def delete_verification_code_from_redis(email: str):
        """从Redis中删除验证码"""
        await RedisClient.delete(email)

    @staticmethod
    async def set_verification_code_to_redis(email: str, code: str, expire: int = CODE_EXPIRATION):
        """将验证码存储到Redis中"""
        await RedisClient.set(email, code, expire=expire)

    @staticmethod
    async def get_or_create_sports_info(user_id: int):
        """获取/创建用户运动信息"""
        return await UserSportsInfo.get_or_create_sports_info(user_id=user_id)

    @staticmethod
    async def create_new_train(sports_info, name: str, duration: float, start_date, end_date, actions: List[dict]):
        """新建训练"""
        return await Train.create_new_train(
            sports_info=sports_info,
            name=name,
            duration=duration,
            start_date=start_date,
            end_date=end_date,
            actions=actions
        )

    @staticmethod
    async def create_new_aerobic(sports_info,name:str,aerobic_type: Literal["steady", "interval"],really_time:float,target_time:int,start_date,end_date,interval_items:List[dict]=None):
        """新建有氧记录"""
        return await Aerobic.create_new_aerobic(
            sports_info=sports_info,
            name=name,
            type=aerobic_type,
            really_time=really_time,
            target_time=target_time,
            start_date=start_date,
            end_date=end_date,
            items=interval_items if type == "interval" else None
        )

    @staticmethod
    async def add_duration(user_id: int, duration: float):
        """增加运动时长"""
        await UserSportsInfo.add_duration(user_id, duration)

