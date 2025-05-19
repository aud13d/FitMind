from fastapi import APIRouter
from ..schemas.train import *
from ..services.trainService import TrainService

router = APIRouter(prefix="/train", tags=["Train"])

# 训练完成
@router.post("/finish")
async def finish(train:TrainFinishRequest):
    """接收客户端的训练完成请求"""
    response = await TrainService.finish_train(
        user_id=train.user_id,
        name=train.name,
        duration=train.duration,
        start_date=train.start_date,
        end_date=train.end_date,
        actions=train.actions
    )

    return response


