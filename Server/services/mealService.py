from Server.services.dataService import DataService
from Server.schemas.meal import FoodResponse

class MealService:
    @staticmethod
    async def search_food(food:str):
        """根据关键字从数据库中查找数据"""
        foods = await DataService.search_food(food)
        return [
            FoodResponse(
                id=f.id,
                name=f.name,
                energy_kcal=f.energy_kcal,
                protein_g=f.protein_g,
                carbs_g=f.carbs_g,
                fat_g=f.fat_g,
            )
            for f in foods
        ]