from datetime import date, datetime
from tortoise import fields
from tortoise.models import Model
from tortoise.exceptions import DoesNotExist

class UserDietInfo(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField('models.User', related_name='diet_infos')
    date = fields.DateField()  # 代表这条数据是哪一天的

    current_kcal = fields.FloatField(default=0.0)  # 当前摄入千卡
    protein = fields.FloatField(default=0.0)         # 蛋白质 g
    carbohydrate = fields.FloatField(default=0.0)    # 碳水化合物 g
    fat = fields.FloatField(default=0.0)             # 脂肪 g
    water = fields.FloatField(default=0.0)           # 饮水量 ml
    target_kcal = fields.FloatField(default=0.0)     # 目标千卡

    create_at = fields.DatetimeField(auto_now_add=True)
    update_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "user_diet_infos"
        unique_together = ("user", "date")  # 用户+日期唯一，确保每天只有一条数据

    @classmethod
    async def get_or_create_diet_info(cls, user_id: int, date_: date = None, target_kcal: float = None):
        if not date_:
            date_ = date.today()
        try:
            return await cls.get(user_id=user_id, date=date_)
        except DoesNotExist:
            # 优先使用传入的 target_kcal
            if target_kcal is not None:
                pass  # 使用传入值
            else:
                # 否则查找最近一次记录的目标
                recent = await cls.filter(user_id=user_id, date__lt=date_) \
                    .order_by("-date") \
                    .first()
                target_kcal = recent.target_kcal if recent else 0.0
            return await cls.create(user_id=user_id, date=date_, target_kcal=target_kcal)

    @classmethod
    async def add_nutrition(cls, user_id: int, date_: date = None,
                            calorie_increment: float = 0.0,
                            protein_increment: float = 0.0,
                            carbohydrate_increment: float = 0.0,
                            fat_increment: float = 0.0,
                            water_increment: float = 0.0):
        diet_info = await cls.get_or_create_diet_info(user_id, date_)
        diet_info.current_kcal += calorie_increment
        diet_info.protein += protein_increment
        diet_info.carbohydrate += carbohydrate_increment
        diet_info.fat += fat_increment
        diet_info.water += water_increment
        await diet_info.save()
        return diet_info

    @classmethod
    async def get_diet_info(cls, user_id: int, date_: date = None):
        """
        查询指定用户指定日期的饮食信息，没有就返回 None
        """
        if not date_:
            date_ = date.today()
        try:
            return await cls.get(user_id=user_id, date=date_)
        except DoesNotExist:
            return None

    def to_dict(self):
        return {
            "user": self.user,
            "date": self.date.isoformat(),
            "calorie_intake": self.calorie_intake,
            "protein": self.protein,
            "carbohydrate": self.carbohydrate,
            "fat": self.fat,
            "water": self.water,
            "current_kcal": self.current_kcal,
            "target_kcal": self.target_kcal,
            "create_at": self.create_at.isoformat(),
            "update_at": self.update_at.isoformat(),
        }
