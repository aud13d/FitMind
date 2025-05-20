from fastapi import APIRouter
from ..schemas.aerobic import *
from ..services.aerobicService import AerobicService

router = APIRouter(prefix="/aerobic", tags=["Aerobic"])

# 有氧训练完成
@router.post("/complete")
async def confirm(aerobic: AerobicConfirmRequest):
    """接收客户端的有氧训练完成请求"""
    response = await AerobicService.confirm_aerobic(
        user_id=aerobic.user_id,
        name=aerobic.name,
        aerobic_type=aerobic.type,
        really_time=aerobic.really_time,
        target_time=aerobic.target_time,
        start_date=aerobic.start_date,
        end_date=aerobic.end_date,
        interval_reminder=aerobic.interval_reminder,
        interval_items=aerobic.interval_items
    )
    return response
