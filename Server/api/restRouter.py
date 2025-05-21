from fastapi import APIRouter
from ..schemas.rest import *
from ..services.restService import RestService

router = APIRouter(prefix="/rest", tags=["Rest"])

@router.post("/save")
async def save(rest: RestSave):
    """接收客户端的休息时间保存请求"""
    response = await RestService.save_rest(
        user_id=rest.user_id,
        title=rest.title,
        date=rest.date,
        color=rest.color
        )

    return response


