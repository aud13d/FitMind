from tortoise import fields
from tortoise.models import Model

class MealItem(Model):
    id = fields.IntField(pk=True)
    meal = fields.ForeignKeyField('models.Meal', related_name='meal_item')
    food_name = fields.CharField(max_length=100)
    weight = fields.FloatField(default=0.0)
    energy = fields.FloatField(default=0.0)
    protein = fields.FloatField(default=0.0)
    carbs = fields.FloatField(default=0.0)
    fat = fields.FloatField(default=0.0)

    class Meta:
        table = "meal_items"

    async def save_with_sync(self):
        await self.save()
        meal = await self.meal
        await meal.recalculate_totals()
