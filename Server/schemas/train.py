from datetime import datetime
from pydantic import BaseModel

class TrainItem(BaseModel):
    name: str # 动作名称
    sets: int # 组数
    reps: int # 每组次数
    rest_time: float # 组间休息时间
    order: int # 动作顺序
    note: str # 备注

class TrainFinishRequest(BaseModel):
    user_id:int # 用户id
    name: str  # 训练名称
    duration: float  # 总时长
    start_date: datetime  # 开始时间
    end_date: datetime  # 结束时间
    actions: list[TrainItem]  # 动作详情