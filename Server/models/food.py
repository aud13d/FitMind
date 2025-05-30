# models/food.py
from tortoise.models import Model
from tortoise import fields

class Food(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    energy_kcal = fields.FloatField(null=True)       # 热量
    protein_g = fields.FloatField(null=True)         # 蛋白质
    carbs_g = fields.FloatField(null=True)           # 碳水
    fat_g = fields.FloatField(null=True)             # 脂肪

    class Meta:
        table = "food"

    @classmethod
    async def search_by_keyword(cls, keyword: str, limit: int = 10):
        return await cls.filter(name__icontains=keyword).limit(limit)