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