from tortoise.models import Model
from tortoise import fields

from Server.models.weightHistory import WeightHistory


class Weight(Model):
    id = fields.IntField(pk=True)
    body_info = fields.OneToOneField('models.UserBodyInfo', related_name='weight')
    current_weight = fields.FloatField(default=0.0)  # 当前体重
    target_weight = fields.FloatField(default=0.0)  # 目标体重
    body_fat_rate = fields.FloatField(default=0.0)  # 体脂率

    created_at = fields.DatetimeField(auto_now_add=True)
    update_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "weight"

    @classmethod
    async def create_or_update(cls, body_info, current_weight: float = None, target_weight: float = None, body_fat_rate: float = None):
        """创建或更新体重信息，并按需记录历史"""
        obj = await cls.get_or_none(body_info=body_info)

        if obj:
            # 判断是否传了体重和体脂（非 None）
            weight_provided = current_weight is not None
            fat_provided = body_fat_rate is not None

            # 更新对应字段
            if weight_provided:
                obj.current_weight = current_weight
            if target_weight is not None:
                obj.target_weight = target_weight
            if fat_provided:
                obj.body_fat_rate = body_fat_rate

            await obj.save()

            # 只要传了且非空就记录历史
            await WeightHistory.record_history(
                weight_data=obj,
                weight=current_weight if weight_provided else None,
                body_fat_rate=body_fat_rate if fat_provided else None
            )

        else:
            # 新建时体重和体脂需要传，不传可能报错
            obj = await cls.create(
                body_info=body_info,
                current_weight=current_weight if current_weight is not None else 0.0,
                target_weight=target_weight if target_weight is not None else 0.0,
                body_fat_rate=body_fat_rate if body_fat_rate is not None else 0.0
            )
            # 初次创建，记录全部传的字段（体重和体脂都传才记录）
            await WeightHistory.record_history(
                weight_data=obj,
                weight=current_weight,
                body_fat_rate=body_fat_rate
            )

        return obj

    @classmethod
    async def get_by_user(cls, body_info):
        """通过 body_info 获取体重数据"""
        return await cls.get_or_none(body_info=body_info)

    @classmethod
    async def get_current_weight(cls, body_info):
        weight_data = await cls.get_by_user(body_info)
        if not weight_data:
            return None
        return weight_data.current_weight

    @classmethod
    async def get_target_weight(cls, body_info):
        weight_data = await cls.get_by_user(body_info)
        if not weight_data:
            return None
        return weight_data.target_weight

    @classmethod
    async def get_current_body_fat_rate(cls, body_info):
        weight_data = await cls.get_by_user(body_info)
        if not weight_data:
            return None
        return weight_data.body_fat_rate


