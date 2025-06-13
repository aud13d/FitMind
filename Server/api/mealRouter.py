from fastapi import APIRouter
from ..schemas.meal import *
from ..services.mealService import MealService

router = APIRouter(prefix="/meal", tags=["Meal"])

@router.post("/food/search_food")
async def search_food(query: FoodQuery):
    response = await MealService.search_food(query.keyword)
    return response

@router.post("/add_meal")
async def add_meal(meal: MealSaveRequest):
    response = await MealService.add_meal(
        user_id = meal.user_id,
        target_kcal = meal.target_kcal,
        foods = meal.foods
    )
    return response