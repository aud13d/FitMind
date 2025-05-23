from tortoise.exceptions import DoesNotExist
from tortoise.models import Model
from tortoise import fields

class UserBodyInfo(Model):
    id = fields.IntField(pk=True)
    user = fields.OneToOneField('models.User', related_name='body_info')
    gender = fields.CharField(max_length=10, null=True)  # 性别
    birthday = fields.DateField(null=True)               # 出生日期
    height = fields.FloatField(null=True)                # 身高（cm）

    create_at=fields.DatetimeField(auto_now_add=True)
    update_at=fields.DatetimeField(auto_now=True)

    class Meta:
        table = "user_body_infos"

    @classmethod
    async def get_body_info(cls, user_id: int):
        """获取用户身体信息"""
        return await cls.get(user_id=user_id)

    @classmethod
    async def create_body_info(cls, user_id: int,gender: str=None, birthday: str=None, height: float=None):
        """为用户创建身体信息"""
        return await cls.create(user_id=user_id,gender=gender, birthday=birthday, height=height)

    @classmethod
    async def get_or_create_body_info(cls, user_id: int, gender: str=None, birthday: str=None, height: float=None):
        """获取或创建用户身体信息"""
        try:
            return await cls.get(user_id=user_id)
        except DoesNotExist:
            return await cls.create_body_info(user_id=user_id, gender=gender, birthday=birthday, height=height)

    @classmethod
    async def update_body_info(cls, user_id: int, gender: str, birthday: str, height: float):
        """更新用户身体信息"""
        body_info = await cls.get_body_info(user_id)
        if body_info:
            body_info.gender = gender
            body_info.birthday = birthday
            body_info.height = height
            await body_info.save()
            return body_info
        else:
            return await cls.create_body_info(user_id=user_id, gender=gender, birthday=birthday, height=height)

