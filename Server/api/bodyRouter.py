from fastapi import APIRouter
from ..schemas.body import *
from ..services.circumferenceService import CircumferenceService
from ..services.weightService import WeightService

router = APIRouter(prefix="/body", tags=["Body"])

@router.post("/get_latest_body_data")
async def get_latest_body_data(body_data:GetBodyDataRequest):
    weight_info = await WeightService.get_latest_weight_and_fat(body_data.user_id)
    circumference_info = await CircumferenceService.get_latest_circumference(body_data.user_id)

    return {
        **weight_info,
        "circumference": circumference_info
    }
