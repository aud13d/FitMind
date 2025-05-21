from fastapi import HTTPException
from datetime import  date
from Server.services.dataService import DataService
from .config import *

class RestService:
    @staticmethod
    async def save_rest(user_id: int, title: str, date: date, color: str):
        """保存休息逻辑"""
        # 查询用户的运动信息（外键）
        sports_info = await DataService.get_or_create_sports_info(user_id)
        if not sports_info:
            raise HTTPException(status_code=400, detail=REST_SPORTS_INFO_NOT_EXIST)

        # 创建休息记录
        if not await DataService.create_new_rest(sports_info=sports_info, title=title, date=date, color=color):
            raise HTTPException(status_code=400, detail=REST_CREATE_FAILED)

        return {"message": REST_SAVE}
