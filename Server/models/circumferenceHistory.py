from datetime import date

from tortoise.expressions import Q
from tortoise.models import Model
from tortoise import fields


class CircumferenceHistory(Model):
    id = fields.IntField(pk=True)
    circumference = fields.ForeignKeyField('models.Circumference', related_name='circumference_history')

    neck = fields.FloatField(null=True)
    shoulder = fields.FloatField(null=True)
    chest = fields.FloatField(null=True)
    waist = fields.FloatField(null=True)
    hip = fields.FloatField(null=True)
    arm_left = fields.FloatField(null=True)
    arm_right = fields.FloatField(null=True)
    forearm_left = fields.FloatField(null=True)
    forearm_right = fields.FloatField(null=True)
    thigh_left = fields.FloatField(null=True)
    thigh_right = fields.FloatField(null=True)
    calf_left = fields.FloatField(null=True)
    calf_right = fields.FloatField(null=True)

    record_date = fields.DateField(auto_now_add=True)

    class Meta:
        table = "circumference_histories"

    @classmethod
    async def record_history(cls, circumference, data: dict):
        """记录围度历史（按天唯一）"""
        if not data:
            return None

        today = date.today()
        existing = await cls.get_or_none(circumference=circumference, record_date=today)

        if existing:
            for key, value in data.items():
                setattr(existing, key, value)
            await existing.save()
            return existing
        else:
            return await cls.create(
                circumference=circumference,
                record_date=today,
                **data
            )

    @classmethod
    async def get_latest_circumference(cls, circumference):
        """获取每个字段最近一次的非空值和记录日期"""
        fields = [
            "neck", "shoulder", "chest", "waist", "hip",
            "arm_left", "arm_right", "forearm_left", "forearm_right",
            "thigh_left", "thigh_right", "calf_left", "calf_right"
        ]

        result = {}

        for field in fields:
            latest = (
                await cls.filter(
                    Q(circumference=circumference) & ~Q(**{field: None})
                )
                .order_by("-record_date")
                .first()
            )
            if latest:
                result[field] = {
                    "value": getattr(latest, field),
                    "date": str(latest.record_date)
                }
            else:
                result[field] = {
                    "value": None,
                    "date": None
                }

        return result

