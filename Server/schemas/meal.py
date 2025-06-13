from typing import Optional

from pydantic import BaseModel
class FoodQuery(BaseModel):
    keyword: str

class FoodResponse(BaseModel):
    id: int
    name: str
    energy_kcal: Optional[float]
    protein_g: Optional[float]
    carbs_g: Optional[float]
    fat_g: Optional[float]

class FoodData(BaseModel):
    food_name:str
    weight:float
    energy: float
    protein: float
    carbs: float
    fat: float

class MealSaveRequest(BaseModel):
    user_id: int
    target_kcal: float
    foods: list[FoodData]
