from datetime import date
from typing import List, Literal

from ..models.aerobic import Aerobic
from ..models.circumference import Circumference
from ..models.circumferenceHistory import CircumferenceHistory
from ..models.food import Food
from ..models.rest import Rest
from ..models.user import User
from ..database.redisClient import RedisClient
from .config import CODE_EXPIRATION
from ..models.userBodyInfo import UserBodyInfo
from ..models.userSportsInfo import UserSportsInfo
from ..models.train import Train
from ..models.weightHistory import WeightHistory
from ..models.weight import Weight


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
            items=interval_items if aerobic_type == "interval" else None
        )

    @staticmethod
    async def create_new_rest(sports_info, title:str, date, color:str):
        """新建休息记录"""
        return await Rest.create_new_rest(
            sports_info=sports_info,
            title=title,
            date=date,
            color=color
        )

    @staticmethod
    async def add_duration(user_id: int, duration: float):
        """增加运动时长"""
        await UserSportsInfo.add_duration(user_id, duration)

    @staticmethod
    async def get_or_create_body_info(user_id: int):
        """获取/创建用户身体数据"""
        return await UserBodyInfo.get_or_create_body_info(user_id=user_id)

    @staticmethod
    async def create_or_update_current_weight(body_info: int, current_weight: float):
        """创建/更新当前体重"""
        return await Weight.create_or_update(body_info, current_weight=current_weight)

    @staticmethod
    async def create_or_update_target_weight(body_info, target_weight: float):
        """创建/更新目标体重"""
        return await Weight.create_or_update(body_info, target_weight=target_weight)

    @staticmethod
    async def create_or_update_body_fat_rate(body_info, body_fat_rate: float):
        """创建/更新体脂率"""
        return await Weight.create_or_update(body_info, body_fat_rate=body_fat_rate)

    @staticmethod
    async def get_current_weight(body_info):
        """获取当前体重"""
        return await Weight.get_current_weight(body_info)

    @staticmethod
    async def get_target_weight(body_info):
        """获取目标体重"""
        return await Weight.get_target_weight(body_info)

    @staticmethod
    async def get_current_body_fat_rate(body_info):
        """获取当前体脂率"""
        return await Weight.get_current_body_fat_rate(body_info)

    @staticmethod
    async def get_weight_history(body_info):
        """获取历史体重"""
        return await WeightHistory.get_weight_history(body_info)

    @staticmethod
    async def get_body_fat_rate_history(body_info):
        """获取历史体脂率"""
        return await WeightHistory.get_body_fat_rate_history(body_info)

    @staticmethod
    async def delete_weight_history_by_date(weight_data, target_date: date):
        """删除特定日期的体重记录"""
        return await WeightHistory.delete_weight_history_by_date(weight_data, target_date)

    @staticmethod
    async  def delete_body_fat_rate_history_by_date(weight_data, target_date: date):
        """删除特定日期的体脂率记录"""
        return await WeightHistory.delete_body_fat_rate_history_by_date(weight_data, target_date)

    @staticmethod
    async def get_weight_by_user(body_info):
        """获取用户体重表"""
        return await Weight.get_by_user(body_info)

    @staticmethod
    async def get_latest_weight(weight_data):
        """根据体重表从对应的历史记录中获取最新体重"""
        return await WeightHistory.get_latest_weight(weight_data)

    @staticmethod
    async def get_latest_body_fat_rate(weight_data):
        """根据体重表从对应的历史记录中获取最新体脂率"""
        return await WeightHistory.get_latest_body_fat_rate(weight_data)


    @staticmethod
    async def create_or_update_current_circumference(body_info,data:dict):
        """创建/更新当前身体围度"""
        return await Circumference.create_or_update(body_info, data)

    @staticmethod
    async def get_circumferences_by_user(body_info):
        """获取用户身体围度表"""
        return await Circumference.get_by_user(body_info)

    @staticmethod
    async def get_latest_circumference(circumference_data):
        """根据身体围度表从对应的历史记录中获取最新的身体围度"""
        return await CircumferenceHistory.get_latest_circumference(circumference_data)

    @staticmethod
    async def get_circumference_history(circumference,part):
        """获取身体围度历史记录"""
        return await CircumferenceHistory.get_circumference_history(circumference,part)

    @staticmethod
    async def delete_circumference_record_by_date(circumference,part,date):
        """删除特定日期的身体围度记录"""
        return await CircumferenceHistory.delete_circumference_history_by_date(circumference,part,date)

    @staticmethod
    async def search_food(food:str):
        """根据关键字从数据库中查找食物数据"""
        return await Food.search_by_keyword(food)