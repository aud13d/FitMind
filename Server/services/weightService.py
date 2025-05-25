from datetime import date

from fastapi import HTTPException
from .config import *
from Server.services.dataService import  DataService

class WeightService:
    @staticmethod
    async def get_latest_weight_and_fat(user_id: int):
        body_info = await DataService.get_or_create_body_info(user_id=user_id)
        if not body_info:
            raise HTTPException(status_code=400, detail=BODY_INFO_NOT_EXIST)

        weight_data = await DataService.get_weight_by_user(body_info)
        weight_history = await DataService.get_latest_weight(weight_data) if weight_data else None
        fat_history = await DataService.get_latest_body_fat_rate(weight_data) if weight_data else None

        def wrap(value, date):
            return {"value": value, "date": str(date) if date else None}

        return {
            "current_weight": wrap(
                weight_history.weight if weight_history else None,
                weight_history.record_date if weight_history else None
            ),
            "body_fat_rate": wrap(
                fat_history.body_fat_rate if fat_history else None,
                fat_history.record_date if fat_history else None
            ),
            "target_weight": weight_data.target_weight if weight_data else None,
        }

    @staticmethod
    async def save_current_weight(user_id:int, current_weight:float):
        """保存当前体重逻辑"""
        # 获取用户身体信息对象
        body_info = await DataService.get_or_create_body_info(user_id=user_id)
        if not body_info:
            raise HTTPException(status_code=400, detail=BODY_INFO_NOT_EXIST)

        if not await DataService.create_or_update_current_weight(body_info, current_weight):
            raise HTTPException(status_code=400, detail=CURRENT_WEIGHT_CREATE_FAILED)

        return {"message": CURRENT_WEIGHT_CREATE_SUCCESSFULLY, "current_weight": current_weight}

    @staticmethod
    async def save_target_weight(user_id:int, target_weight:float):
        """保存目标体重逻辑"""
        # 获取用户身体信息对象
        body_info = await DataService.get_or_create_body_info(user_id=user_id)
        if not body_info:
            raise HTTPException(status_code=400, detail=BODY_INFO_NOT_EXIST)
        if not await DataService.create_or_update_target_weight(body_info, target_weight):
            raise HTTPException(status_code=400, detail=TARGET_WEIGHT_CREATE_FAILED)

        return {"message": TARGET_WEIGHT_CREATE_SUCCESSFULLY, "target_weight": target_weight}

    @staticmethod
    async def save_body_fat_rate(user_id:int, body_fat_rate:float):
        """保存体脂率逻辑"""
        # 获取用户身体信息对象
        body_info = await DataService.get_or_create_body_info(user_id=user_id)
        if not body_info:
            raise HTTPException(status_code=400, detail=BODY_INFO_NOT_EXIST)
        if not await DataService.create_or_update_body_fat_rate(body_info, body_fat_rate):
            raise HTTPException(status_code=400, detail=BODY_FAT_RATE_CREATE_FAILED)

        return {"message": BODY_FAT_RATE_CREATE_SUCCESSFULLY, "body_fat_rate": body_fat_rate}

    @staticmethod
    async def get_current_weight(user_id: int):
        """获取当前体重逻辑"""
        # 获取用户身体信息对象
        body_info = await DataService.get_or_create_body_info(user_id=user_id)
        if not body_info:
            raise HTTPException(status_code=400, detail=BODY_INFO_NOT_EXIST)

        current_weight = await DataService.get_current_weight(body_info)

        if not current_weight:
            raise HTTPException(status_code=400, detail=CURRENT_WEIGHT_NOT_EXIST)

        return {"message": CURRENT_WEIGHT_GET_SUCCESSFULLY, "current_weight": current_weight}

    @staticmethod
    async def get_target_weight(user_id: int):
        """获取目标体重逻辑"""
        # 获取用户身体信息对象
        body_info = await DataService.get_or_create_body_info(user_id=user_id)
        if not body_info:
            raise HTTPException(status_code=400, detail=BODY_INFO_NOT_EXIST)
        target_weight = await DataService.get_target_weight(body_info)
        if not target_weight:
            raise HTTPException(status_code=400, detail=TARGET_WEIGHT_NOT_EXIST)

        return {"message": TARGET_WEIGHT_GET_SUCCESSFULLY, "target_weight": target_weight}

    @staticmethod
    async def get_current_body_fat_rate(user_id: int):
        """获取当前体脂率逻辑"""
        # 获取用户身体信息对象
        body_info = await DataService.get_or_create_body_info(user_id=user_id)
        if not body_info:
            raise HTTPException(status_code=400, detail=BODY_INFO_NOT_EXIST)
        current_body_fat_rate = await DataService.get_current_body_fat_rate(body_info)
        if not current_body_fat_rate:
            raise HTTPException(status_code=400, detail=CURRENT_FAT_NOT_EXIST)

        return {"message": CURRENT_BODY_FAT_RATE_GET_SUCCESSFULLY, "current_body_fat_rate": current_body_fat_rate}

    @staticmethod
    async def get_weight_history(user_id: int):
        """获取体重历史记录"""
        body_info = await DataService.get_or_create_body_info(user_id)
        if not body_info:
            raise HTTPException(status_code=400, detail=BODY_INFO_NOT_EXIST)

        history = await DataService.get_weight_history(body_info)

        if not history:
            raise HTTPException(status_code=400, detail=WEIGHT_HISTORY_NOT_EXIST)

        return {
            "message": WEIGHT_HISTORY_GET_SUCCESSFULLY,
            "weight_history": [
                {
                    "weight": record.weight,
                    "record_date": record.record_date
                }
                for record in history
            ]
        }

    @staticmethod
    async def get_body_fat_rate_history(user_id: int):
        """获取体脂率历史记录"""
        body_info = await DataService.get_or_create_body_info(user_id)
        if not body_info:
            raise HTTPException(status_code=400, detail=BODY_INFO_NOT_EXIST)
        history = await DataService.get_body_fat_rate_history(body_info)

        if not history:
            raise HTTPException(status_code=400, detail=BODY_FAT_RATE_HISTORY_NOT_EXIST)
        return {
            "message": BODY_FAT_RATE_HISTORY_GET_SUCCESSFULLY,
            "body_fat_rate_history": [
                {
                    "body_fat_rate": record.body_fat_rate,
                    "record_date": record.record_date
                }
                for record in history
            ]
        }

    @staticmethod
    async def delete_weight_history_by_date(user_id: int, target_date: date):
        """删除指定日期的体重历史记录"""
        body_info = await DataService.get_or_create_body_info(user_id)
        if not body_info:
            raise HTTPException(status_code=400, detail=BODY_INFO_NOT_EXIST)

        weight_data = await DataService.get_weight_by_user(body_info)

        deleted_count = await DataService.delete_weight_history_by_date(weight_data, target_date)
        if deleted_count == 0:
            raise HTTPException(status_code=400, detail=WEIGHT_HISTORY_NOT_EXIST)


        return {"message": WEIGHT_HISTORY_DELETED_SUCCESSFULLY , "deleted_count": deleted_count}

    @staticmethod
    async def delete_body_fat_rate_history_by_date(user_id: int, target_date: date):
        """删除指定日期的体脂率历史记录"""
        body_info = await DataService.get_or_create_body_info(user_id)
        if not body_info:
            raise HTTPException(status_code=400, detail=BODY_INFO_NOT_EXIST)

        weight_data = await DataService.get_weight_by_user(body_info)

        deleted_count = await DataService.delete_body_fat_rate_history_by_date(weight_data, target_date)
        if deleted_count == 0:
            raise HTTPException(status_code=400, detail=BODY_FAT_RATE_HISTORY_NOT_EXIST)

        return {"message": BODY_FAT_RATE_HISTORY_DELETED_SUCCESSFULLY, "deleted_count": deleted_count}








