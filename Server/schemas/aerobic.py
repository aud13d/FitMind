from datetime import datetime
from typing import Literal, Optional, List
from pydantic import BaseModel

class AerobicItem(BaseModel):
    name: str           # 有氧子项名称，比如变速间隔的具体说明
    duration: float     # 该子项持续时间（秒）
    note: Optional[str] = None  # 备注（可选）

class AerobicConfirmRequest(BaseModel):
    user_id: int                 # 用户id
    name: str                   # 有氧训练名称
    type: Literal["steady", "interval"]  # 类型：匀速 or 变速
    really_time: float           # 实际训练时长(分钟)
    target_time: int  # 目标训练时长(分钟)
    start_date: datetime         # 开始时间
    end_date: datetime           # 结束时间
    interval_reminder: Optional[int] = None  # 变速提醒间隔秒数
    interval_items: Optional[List[AerobicItem]] = None  # 子项详情
