from datetime import datetime
from fastapi import HTTPException
from .config import *
from Server.services.dataService import DataService
from typing import Literal

class AerobicService:
    @staticmethod
    async def confirm_aerobic(user_id: int,name: str,aerobic_type:Literal["steady", "interval"],really_time: float,target_time: int,start_date: datetime,end_date: datetime,interval_reminder: int=None,interval_items: list=None):
        """完成有氧训练逻辑"""
        # 校验有氧时间
        if start_date > end_date:
            raise HTTPException(status_code=400, detail=AEROBIC_START_DATE_AFTER_END_DATE)

        # 校验实际时间
        if really_time < 0:
            raise HTTPException(status_code=400, detail=AEROBIC_DURATION_MUST_BE_POSITIVE)

        # 校验变速项
        if aerobic_type == "interval":
            if not interval_reminder or interval_reminder <= 0:
                raise HTTPException(status_code=400, detail=AEROBIC_INTERVAL_REMINDER_INVALID)
            if not interval_items:
                raise HTTPException(status_code=400, detail=AEROBIC_INTERVAL_ITEMS_REQUIRED)

        # 获取或创建 sports_info
        sports_info = await DataService.get_or_create_sports_info(user_id=user_id)
        if not sports_info:
            raise HTTPException(status_code=400, detail=AEROBIC_SPORTS_INFO_NOT_EXIST)

        # 创建有氧记录
        success = await DataService.create_new_aerobic(
            sports_info=sports_info,
            name=name,
            aerobic_type=aerobic_type,
            really_time=really_time,
            target_time=target_time,
            start_date=start_date,
            end_date=end_date,
            interval_reminder=interval_reminder,
            interval_items=interval_items
        )

        if not success:
            raise HTTPException(status_code=400, detail=AEROBIC_CREATE_FAILED)

        # 更新累计时长
        await DataService.add_duration(user_id, really_time)

        return {"message": AEROBIC_CONFIRM}
