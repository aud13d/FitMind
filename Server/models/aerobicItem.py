from tortoise.models import Model
from tortoise import fields


class AerobicItem(Model):
    id = fields.IntField(pk=True)
    aerobic = fields.ForeignKeyField('models.Aerobic', related_name='aerobic_items')

    speed = fields.FloatField()      # 速度值
    interval = fields.IntField()     # 每隔多少秒变速

    class Meta:
        table = "aerobic_items"

    @classmethod
    async def bulk_create_items(cls, aerobic, items: list[dict]):
        """批量创建变速项，仅包含速度和变速间隔"""
        aerobic_items = [
            cls(
                aerobic=aerobic,
                speed=item["speed"],
                interval=item["interval"]
            )
            for item in items
        ]
        await cls.bulk_create(aerobic_items)
