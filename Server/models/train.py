from typing import List
from datetime import datetime, date, time

from tortoise.models import Model
from tortoise import fields
from Server.models.trainItem import TrainItem


class Train(Model):
    id = fields.IntField(pk=True)
    sports_info = fields.ForeignKeyField('models.UserSportsInfo', related_name='train_plans')
    name = fields.CharField(max_length=255)
    duration = fields.FloatField()
    start_date = fields.DatetimeField()
    end_date = fields.DatetimeField()
    completed = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    update_at = fields.DatetimeField(auto_now=True)
    daily_count = fields.IntField()  # 今日第几次训练

    class Meta:
        table = "trains"

    @classmethod
    async def create_new_train(cls, sports_info, name: str, duration: float, start_date: datetime, end_date: datetime, actions: List[dict]):
        """创建训练记录并自动计算今天第几次训练"""
        train_date: date = start_date.date()

        start_datetime = datetime.combine(train_date, time.min)  # 当天00:00:00
        end_datetime = datetime.combine(train_date, time.max)    # 当天23:59:59.999999

        today_count = await cls.filter(
            sports_info=sports_info,
            start_date__gte=start_datetime,
            start_date__lte=end_datetime
        ).count()

        daily_count = today_count + 1
        if not name:
            name = f"第{daily_count}次训练"

        train = await cls.create(
            sports_info=sports_info,
            name=name,
            duration=duration,
            start_date=start_date,
            end_date=end_date,
            daily_count=daily_count
        )

        await TrainItem.bulk_create_items(train, actions)

        return train
