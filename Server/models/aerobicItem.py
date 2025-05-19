from tortoise.models import Model
from tortoise import fields


class AerobicItem(Model):
    id = fields.IntField(pk=True)
    aerobic = fields.ForeignKeyField('models.Aerobic', related_name='aerobic_items')

    stage_order = fields.IntField()        # 阶段编号（第几阶段）
    speed = fields.FloatField()            # 阶段速度
    duration = fields.FloatField()         # 阶段持续时间（单位：秒）

    class Meta:
        table = "aerobic_items"

    @classmethod
    async def bulk_create_items(cls, aerobic, items: list[dict]):
        """批量创建阶段数据"""
        aerobic_items = [
            cls(
                aerobic=aerobic,
                stage_order=item.get("stage_order", idx + 1),
                speed=item["speed"],
                duration=item["duration"]
            )
            for idx, item in enumerate(items)
        ]
        await cls.bulk_create(aerobic_items)
