from pydantic import BaseModel
class GetBodyDataRequest(BaseModel):
    """获取身体数据请求体"""
    user_id: int