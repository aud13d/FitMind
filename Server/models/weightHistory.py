from datetime import date

from tortoise.models import Model
from tortoise import fields

class WeightHistory(Model):
    id = fields.IntField(pk=True)
    weight_data = fields.ForeignKeyField('models.Weight', related_name='weight_history')
    weight = fields.FloatField(null=True)
    body_fat_rate = fields.FloatField(null=True)
    record_date = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "weight_histories"

    @classmethod
    async def record_history(cls, weight_data, weight: float = None, body_fat_rate: float = None):
        """记录体重或体脂的历史变化"""
        if weight is None and body_fat_rate is None:
            return None
        return await cls.create(
            weight_data=weight_data,
            weight=weight,
            body_fat_rate=body_fat_rate
        )

    @classmethod
    async def get_weight_history(cls, weight_data):
        """获取体重历史记录（排除体脂为空的）"""
        return await cls.filter(weight_data=weight_data).exclude(weight=None).order_by('-record_date')

    @classmethod
    async def get_body_fat_rate_history(cls, weight_data):
        """获取体脂历史记录（排除体重为空的）"""
        return await cls.filter(weight_data=weight_data).exclude(body_fat_rate=None).order_by('-record_date')

    @classmethod
    async def delete_weight_history_by_date(cls, weight_data, target_date: date):
        """
        删除指定日期的体重记录（只删有体重数据的）
        """
        return await cls.filter(
            weight_data=weight_data,
            record_date__date=target_date
        ).exclude(weight=None).delete()

    @classmethod
    async def delete_body_fat_rate_history_by_date(cls, weight_data, target_date: date):
        """
        删除指定日期的体脂率记录（只删有体脂率数据的）
        """
        return await cls.filter(
            weight_data=weight_data,
            record_date__date=target_date
        ).exclude(body_fat_rate=None).delete()

