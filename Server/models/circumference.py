from tortoise.models import Model
from tortoise import fields

class Circumference(Model):
    id = fields.IntField(pk=True)
    body_info = fields.OneToOneField('models.UserBodyInfo', related_name='circumference_data')

    neck = fields.FloatField(default=0.0)
    shoulder = fields.FloatField(default=0.0)
    chest = fields.FloatField(default=0.0)
    waist = fields.FloatField(default=0.0)
    hip = fields.FloatField(default=0.0)

    arm_left = fields.FloatField(default=0.0)
    arm_right = fields.FloatField(default=0.0)
    forearm_left = fields.FloatField(default=0.0)
    forearm_right = fields.FloatField(default=0.0)
    thigh_left = fields.FloatField(default=0.0)
    thigh_right = fields.FloatField(default=0.0)
    calf_left = fields.FloatField(default=0.0)
    calf_right = fields.FloatField(default=0.0)

    created_at = fields.DatetimeField(auto_now_add=True)
    update_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "circumferences"

    @classmethod
    async def create_or_update(cls, body_info, data: dict):
        """创建或更新围度数据（从 dict 字典传入）"""
        obj = await cls.get_or_none(body_info=body_info)
        if obj:
            for key, value in data.items():
                setattr(obj, key, value)
            await obj.save()
        else:
            obj = await cls.create(body_info=body_info, **data)
        return obj

    @classmethod
    async def get_by_user(cls, body_info):
        """通过 body_info 获取围度数据"""
        return await cls.get_or_none(body_info=body_info)
