from pydantic import BaseModel
from datetime import date



class SaveCurrentWeightRequest(BaseModel):
    """保存当前体重请求体"""
    user_id: int
    current_weight: float

class GetCurrentWeightRequest(BaseModel):
    """获取当前体重请求体"""
    user_id: int

class GetWeightHistoryRequest(BaseModel):
    """获取体重历史请求体"""
    user_id: int

class DeleteWeightHistoryRequest(BaseModel):
    """删除特定日期的体重记录请求体"""
    user_id:int
    date: date  # 要删除的体重记录的日期

class SaveTargetWeightRequest(BaseModel):
    """保存目标体重请求体"""
    user_id: int
    target_weight: float

class GetTargetWeightRequest(BaseModel):
    """获取目标体重请求体"""
    user_id: int

class SaveBodyFatRateRequest(BaseModel):
    """保存体脂率请求体"""
    user_id: int
    body_fat_rate: float

class GetCurrentBodyFatRateRequest(BaseModel):
    """获取当前体脂率请求体"""
    user_id: int

class GetBodyFatRateHistoryRequest(BaseModel):
    """获取体脂率历史请求体"""
    user_id: int

class DeleteBodyFatRateHistoryRequest(BaseModel):
    """删除特定日期的体脂率记录请求体"""
    user_id:int
    date: date  # 要删除的体脂率记录的日期

