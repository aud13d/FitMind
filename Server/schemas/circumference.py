from typing import Literal
from pydantic import BaseModel
from datetime import date

class SaveCurrentCircumferenceRequest(BaseModel):
    user_id: int
    part: Literal[
        "neck", "shoulder", "chest", "waist", "hip",
        "arm_left", "arm_right", "forearm_left", "forearm_right",
        "thigh_left", "thigh_right", "calf_left", "calf_right"
    ]
    value: float

class GetCurrentNeckRequest(BaseModel):
    """获取当前体重请求体"""
    user_id: int

class GetNeckHistoryRequest(BaseModel):
    """获取体重历史请求体"""
    user_id: int

class DeleteNeckHistoryRequest(BaseModel):
    """删除特定日期的体重记录请求体"""
    user_id:int
    date: date  # 要删除的体重记录的日期