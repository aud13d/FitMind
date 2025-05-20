from datetime import datetime
from fastapi import HTTPException
from .config import *
from Server.services.dataService import DataService
from typing import Literal

class AerobicService:
    @staticmethod
    async def confirm_aerobic(user_id: int,name: str,aerobic_type:Literal["steady", "interval"],really_time: float,target_time: int,start_date: datetime,end_date: datetime,interval_items: list=None):
        """完成有氧训练逻辑"""
        if start_date > end_date:
            raise HTTPException(status_code=400, detail=AEROBIC_START_DATE_AFTER_END_DATE)

        if really_time < 0:
            raise HTTPException(status_code=400, detail=AEROBIC_DURATION_MUST_BE_POSITIVE)

        if aerobic_type == "interval":
            if not interval_items or len(interval_items) == 0:
                raise HTTPException(status_code=400, detail=AEROBIC_INTERVAL_ITEMS_REQUIRED)

        sports_info = await DataService.get_or_create_sports_info(user_id=user_id)
        if not sports_info:
            raise HTTPException(status_code=400, detail=AEROBIC_SPORTS_INFO_NOT_EXIST)

        # 创建记录
        success = await DataService.create_new_aerobic(
            sports_info=sports_info,
            name=name,
            aerobic_type=aerobic_type,
            really_time=really_time,
            target_time=target_time,
            start_date=start_date,
            end_date=end_date,
            interval_items=interval_items
        )

        if not success:
            raise HTTPException(status_code=400, detail=AEROBIC_CREATE_FAILED)

        await DataService.add_duration(user_id, really_time)

        return {"message": AEROBIC_CONFIRM}
