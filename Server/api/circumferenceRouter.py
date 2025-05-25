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

# 获取身体围度表历史记录
@router.post("/get_circumference_history")
async def get_circumference_history(history: GetCircumferenceHistoryRequest):
    """获取身体部位的围度历史数据"""
    response = await CircumferenceService.get_circumference_history(
        user_id=history.user_id,
        part=history.part
    )
    return response

# 删除特定日期的身体围度记录
@router.post("/delete_circumference_record")
async def delete_circumference_record_by_date(circumference: DeleteCircumferenceRecordRequest):
    """删除特定日期的身体围度记录"""
    response = await CircumferenceService.delete_circumference_record_by_date(
        user_id=circumference.user_id,
        part=circumference.part,
        date=circumference.date
    )
    return response



