from datetime import datetime, date, time
from typing import Literal, Optional, List

from tortoise.models import Model
from tortoise import fields
from Server.models.aerobicItem import AerobicItem


class Aerobic(Model):
    id = fields.IntField(pk=True)
    sports_info = fields.ForeignKeyField('models.UserSportsInfo', related_name='aerobics')

    name = fields.CharField(max_length=255)
    type = fields.CharField(max_length=16)
    really_time = fields.FloatField()
    target_time = fields.FloatField()
    start_date = fields.DatetimeField()
    end_date = fields.DatetimeField()
    interval_reminder = fields.IntField(null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    daily_count = fields.IntField()
    aerobic_items: fields.ReverseRelation["AerobicItem"]

    class Meta:
        table = "aerobics"

    @classmethod
    async def create_new_aerobic(cls,sports_info,name: str,type: Literal["steady", "interval"],really_time: float,target_time:int,start_date: datetime,end_date: datetime,interval_reminder: Optional[int] = None,items: Optional[List[dict]] = None ):
        """创建有氧记录，并在变速类型下创建子项"""
        aerobic_date: date = start_date.date()

        start_datetime = datetime.combine(aerobic_date, time.min)
        end_datetime = datetime.combine(aerobic_date, time.max)

        today_count = await cls.filter(
            sports_info=sports_info,
            start_date__gte=start_datetime,
            start_date__lte=end_datetime
        ).count()

        daily_count = today_count + 1

        aerobic = await cls.create(
            sports_info=sports_info,
            name=name,
            type=type,
            really_time=really_time,
            target_time=target_time,
            start_date=start_date,
            end_date=end_date,
            interval_reminder=interval_reminder if type == "interval" else None,
            daily_count=daily_count
        )

        if type == "interval" and items:
            await AerobicItem.bulk_create_items(aerobic, items)

        return aerobic
