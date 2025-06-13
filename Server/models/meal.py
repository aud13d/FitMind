from tortoise.models import Model
from tortoise import fields

from Server.models.mealItem import MealItem


class Meal(Model):
    id = fields.IntField(pk=True)
    user_diet_info = fields.ForeignKeyField('models.UserDietInfo', related_name='meals')
    meal_type = fields.CharField(max_length=20)  # e.g., breakfast, lunch

    total_energy = fields.FloatField(default=0.0)
    total_protein = fields.FloatField(default=0.0)
    total_carbs = fields.FloatField(default=0.0)
    total_fat = fields.FloatField(default=0.0)

    create_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "meals"
        unique_together = ("user_diet_info", "meal_type")  # 可选，一天同类餐只存一次

    @classmethod
    async def create_with_items(cls, user_diet_info, meal_type, items: list[dict]):
        # 检查是否已存在该用户同类型的餐
        existing = await cls.get_or_none(user_diet_info=user_diet_info, meal_type=meal_type)
        if existing:
            # raise ValueError(f"Meal of type '{meal_type}' already exists for this user.")

            # 或者你想覆盖旧数据：
            await existing.meal_item.all().delete()
            await existing.add_items(items)
            return existing

        meal = await cls.create(
            user_diet_info=user_diet_info,
            meal_type=meal_type
        )
        await meal.add_items(items)
        return meal

    async def add_items(self, items: list[dict]):
        from Server.models.mealItem import MealItem
        meal_items = [MealItem(meal=self, **item) for item in items]
        await MealItem.bulk_create(meal_items)
        await self.recalculate_totals()

    async def recalculate_totals(self):
        items = await self.meal_item.all()
        self.total_energy = sum(i.energy for i in items)
        self.total_protein = sum(i.protein for i in items)
        self.total_carbs = sum(i.carbs for i in items)
        self.total_fat = sum(i.fat for i in items)
        await self.save()
