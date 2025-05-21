from tortoise import Model
from tortoise import fields

class Rest(Model):
    id = fields.IntField(pk=True)
    sports_info = fields.ForeignKeyField("models.UserSportsInfo", related_name="rests")

    title = fields.CharField(max_length=255)
    date = fields.DateField()
    color = fields.CharField(max_length=7)

    create_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "rests"

    @classmethod
    async def create_new_rest(cls, sports_info: int, title: str, date, color: str):
        """创建休息记录"""
        rest = await cls.create(
            sports_info=sports_info,
            title=title,
            date=date,
            color=color
        )
        return rest

