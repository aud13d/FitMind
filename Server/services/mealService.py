from datetime import datetime

from Server.services.dataService import DataService
from Server.schemas.meal import FoodResponse,FoodData
from fastapi import HTTPException
from .config import *

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

    @staticmethod
    async def add_meal(user_id: int, target_kcal: float, foods: list[FoodData]):
        if not foods:
            raise HTTPException(status_code=400, detail=MEAL_FOOD_LIST_EMPTY)

        now = datetime.now()
        today = now.date()
        meal_type = MealService.get_meal_type_by_time(now)

        user_diet_info = await DataService.get_or_create_user_diet_info(
            user_id=user_id, target_kcal=target_kcal
        )
        if not user_diet_info:
            raise HTTPException(status_code=400, detail=MEAL_USER_DIET_INFO_NOT_FOUND)

        items = [food.model_dump() for food in foods]
        meal = await DataService.create_meal_with_items(user_diet_info, meal_type, items)

        total_energy = sum(f.energy for f in foods)
        total_protein = sum(f.protein for f in foods)
        total_carbs = sum(f.carbs for f in foods)
        total_fat = sum(f.fat for f in foods)

        await DataService.add_nutrition(
            user_id=user_id,
            date=today,
            calorie_increment=total_energy,
            protein_increment=total_protein,
            carbs_increment=total_carbs,
            fat_increment=total_fat
        )

        return {
            "message": MEAL_ADD_SUCCESS,
            "meal_id": meal.id,
        }

    @staticmethod
    def get_meal_type_by_time(now: datetime) -> str:
        """根据时间自动判断早餐、午餐、晚餐"""
        hour = now.hour
        if hour < 10:
            return "Breakfast"
        elif hour < 15:
            return "Lunch"
        else:
            return "Dinner"



