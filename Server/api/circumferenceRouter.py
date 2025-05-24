from fastapi import APIRouter
from ..schemas.circumference import *
from ..services.circumferenceService import CircumferenceService

router = APIRouter(prefix="/body/circumference", tags=["Circumference"])

# 保存当前身体围度
@router.post("/save_current_circumference")
async def save_current_circumference(current_circumference: SaveCurrentCircumferenceRequest):
    """统一保存某个身体部位的围度数据"""
    response = await CircumferenceService.save_current_circumference(
        user_id=current_circumference.user_id,
        part=current_circumference.part,
        value=current_circumference.value
    )
    return response

