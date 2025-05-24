from Server.services.dataService import DataService
from fastapi import HTTPException
from .config import *


class CircumferenceService:
    @staticmethod
    async def get_latest_circumference(user_id: int):
        body_info = await DataService.get_or_create_body_info(user_id=user_id)
        if not body_info:
            raise HTTPException(status_code=400, detail=BODY_INFO_NOT_EXIST)

        circumference_data = await DataService.get_circumferences_by_user(body_info)
        if not circumference_data:
            return {}

        return await DataService.get_latest_circumference(circumference_data)

    @staticmethod
    async def save_current_circumference(user_id: int, part: str, value: float):
        """保存当前身体围度逻辑"""
        body_info = await DataService.get_or_create_body_info(user_id=user_id)
        if not body_info:
            raise HTTPException(status_code=400, detail=BODY_INFO_NOT_EXIST)

        data = {part: value}

        circumference = await DataService.create_or_update_current_circumference(body_info, data)

        if not circumference:
            raise HTTPException(status_code=400, detail=SAVE_CURRENT_CIRCUMFERENCE_FAILED)

        return {"message": CURRENT_CIRCUMFERENCE_SAVE_SUCCESSFULLY, "data": circumference}


