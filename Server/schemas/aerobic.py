from datetime import datetime
from typing import Literal, Optional, List
from pydantic import BaseModel

class AerobicItem(BaseModel):
    interval: int
    speed: float

class AerobicConfirmRequest(BaseModel):
    user_id: int                 # 用户id
    name: str                   # 有氧训练名称
    type: Literal["steady", "interval"]  # 类型：匀速 or 变速
    really_time: float           # 实际训练时长(分钟)
    target_time: int  # 目标训练时长(分钟)
    start_date: datetime         # 开始时间
    end_date: datetime           # 结束时间
    interval_items: Optional[List[AerobicItem]] = None  # 子项详情
