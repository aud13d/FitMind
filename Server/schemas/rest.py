from datetime import date
from pydantic import BaseModel


class RestSave(BaseModel):
    user_id: int
    title: str
    date: date
    color: str
