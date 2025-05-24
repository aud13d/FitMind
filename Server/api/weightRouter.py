from fastapi import APIRouter
from ..schemas.weight import *
from ..services.weightService import WeightService

router = APIRouter(prefix="/body/weight", tags=["Weight"])
# 保存当前体重
@router.post("/save_current_weight")
async def save_current_weight(weight: SaveCurrentWeightRequest):
    """接收客户端的保存当前体重请求"""
    response = await WeightService.save_current_weight(
        user_id=weight.user_id,
        current_weight = weight.current_weight
    )

    return response

# 保存目标体重
@router.post("/save_target_weight")
async def save_target_weight(target_weight: SaveTargetWeightRequest):
    """接收客户端的保存目标体重请求"""
    response = await WeightService.save_target_weight(
        user_id=target_weight.user_id,
        target_weight=target_weight.target_weight
    )
    return response

# 保存体脂率
@router.post("/save_current_body_fat_rate")
async def save_body_fat_rate(body_fat_rate: SaveBodyFatRateRequest):
    """接收客户端的保存体脂率请求"""
    response = await WeightService.save_body_fat_rate(
        user_id=body_fat_rate.user_id,
        body_fat_rate=body_fat_rate.body_fat_rate
    )
    return response

# 获取当前体重
@router.post("/get_current_weight")
async def get_current_weight(weight: GetCurrentWeightRequest):
    """接收客户端的获取当前体重请求"""
    response = await WeightService.get_current_weight(
        user_id=weight.user_id,
    )
    return response

# 获取目标体重
@router.post("/get_target_weight")
async def get_target_weight(target_weight: GetTargetWeightRequest):
    """接收客户端的获取目标体重请求"""
    response = await WeightService.get_target_weight(
        user_id=target_weight.user_id,
    )
    return response

# 获取体脂率
@router.post("/get_body_fat_rate")
async def get_body_fat_rate(body_fat_rate: GetCurrentBodyFatRateRequest):
    """接收客户端的获取体脂率请求"""
    response = await WeightService.get_current_body_fat_rate(
        user_id=body_fat_rate.user_id,
    )
    return response

# 获取体重历史记录
@router.post("/get_weight_history")
async def get_weight_history(history: GetWeightHistoryRequest):
    """获取体重历史记录"""
    response = await WeightService.get_weight_history(
        user_id=history.user_id,
    )
    return response

# 获取体脂率历史记录
@router.post("/get_body_fat_rate_history")
async def get_body_fat_rate_history(history: GetBodyFatRateHistoryRequest):
    """获取体脂历史记录"""
    response = await WeightService.get_body_fat_rate_history(
        user_id=history.user_id,
    )
    return response

# 删除特定日期的体重记录
@router.post("/delete_weight_by_date")
async def delete_weight_by_date(weight: DeleteWeightHistoryRequest):
    """删除特定日期的体重记录"""
    response = await WeightService.delete_weight_history_by_date(
        user_id=weight.user_id,
        target_date=weight.date,
    )
    return response

# 删除特定日期的体脂率记录
@router.post("/delete_body_fat_rate_by_date")
async def delete_body_fat_rate_by_date(body_fat_rate: DeleteBodyFatRateHistoryRequest):
    """删除特定日期的体脂率记录"""
    response = await WeightService.delete_body_fat_rate_history_by_date(
        user_id=body_fat_rate.user_id,
        target_date=body_fat_rate.date,
    )
    return response




