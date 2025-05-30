from fastapi import APIRouter
from ..schemas.meal import *
from ..services.mealService import MealService

router = APIRouter(prefix="/meal", tags=["Meal"])

@router.post("/food/search_food")
async def search_food(query: FoodQuery):
    response = await MealService.search_food(query.keyword)
    return response
