from tortoise.models import Model
from tortoise import fields

class TrainItem(Model):
    id = fields.IntField(pk=True)
    train = fields.ForeignKeyField('models.Train', related_name='items')  # 属于哪个
    name = fields.CharField(max_length=100)  # 动作名称
    # duration = fields.FloatField(null=True)  # 动作持续时间（分钟）
    sets = fields.IntField(null=True)        # 组数
    reps = fields.IntField(null=True)        # 每组次数
    rest_time = fields.FloatField(null=True) # 组间休息时间（秒）
    order = fields.IntField(null=True)       # 排序编号，用于前端排序显示
    note = fields.TextField(null=True)       # 附注（动作要求）

    created_at = fields.DatetimeField(auto_now_add=True)
    update_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "train_items"

    @classmethod
    async def bulk_create_items(cls, train, actions: list):
        """批量创建训练动作"""
        for action in actions:
            await cls.create(
                train=train,
                name=action.name,
                sets=action.sets,
                reps=action.reps,
                rest_time=action.rest_time,
                order=action.order,
                note=action.note
            )

