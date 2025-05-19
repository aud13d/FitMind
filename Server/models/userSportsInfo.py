from tortoise.exceptions import DoesNotExist
from tortoise.models import Model
from tortoise import fields

class UserSportsInfo(Model):
    id = fields.IntField(pk=True)  # id 会自动分配
    user = fields.OneToOneField('models.User', related_name='sports_info')
    total_duration = fields.FloatField(default=0.0)  # 总时长
    total_distance = fields.FloatField(default=0.0)  # 总距离
    total_calories = fields.FloatField(default=0.0)  # 总卡路里
    create_at=fields.DatetimeField(auto_now_add=True)
    update_at=fields.DatetimeField(auto_now=True)

    class Meta:
        table = "user_sports_infos"

    @classmethod
    async def get_sports_info(cls, user_id: int):
        """获取用户运动信息"""
        return await cls.get(user_id=user_id)

    @classmethod
    async def create_sports_info(cls, user_id: int):
        """为用户创建运动信息"""
        return await cls.create(user_id=user_id)

    @classmethod
    async def get_or_create_sports_info(cls, user_id: int):
        """获取或创建用户运动信息"""
        try:
            return await cls.get(user_id=user_id)
        except DoesNotExist:
            return await cls.create(user_id=user_id)

    @classmethod
    async def add_duration(cls, user_id: int, duration: float):
        """增加用户的运动时长"""
        info = await cls.get_sports_info(user_id)
        if info:
            info.total_duration += duration
            await info.save()
            return info
        return None

