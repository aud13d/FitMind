from datetime import datetime
from fastapi import HTTPException
from .config import *
from Server.services.dataService import DataService


class TrainService:
    @staticmethod
    async def finish_train(user_id: int,name: str,duration: float, start_date: datetime,end_date: datetime,actions: list):
        """完成训练逻辑"""
        # 动作校验
        if not actions:
            raise HTTPException(status_code=400, detail=TRAINING_ACTION_EXIST)

        # 时间校验
        if start_date > end_date:
            raise HTTPException(status_code=400, detail=TRAINING_START_DATE_AFTER_END_DATE)

        # 时长校验
        if duration <= 0:
            raise HTTPException(status_code=400, detail=TRAINING_DURATION_MUST_BE_POSITIVE)

        sports_info = await DataService.get_or_create_sports_info(user_id=user_id)

        if not sports_info:
            raise HTTPException(status_code=400, detail=TRAINING_SPORTS_INFO_NOT_EXIST)

        if not await DataService.create_new_train(sports_info, name, duration, start_date, end_date, actions):
            raise HTTPException(status_code=400, detail=TRAINING_CREATE_FAILED)

        await DataService.add_duration(user_id, duration)

        return {"message": TRAINING_FINISH}
