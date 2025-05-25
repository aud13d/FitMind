from typing import Literal
from pydantic import BaseModel
from datetime import date

class SaveCurrentCircumferenceRequest(BaseModel):
    user_id: int
    part: Literal[
        "neck", "shoulder", "chest", "waist", "hip",
        "arm_left", "arm_right", "forearm_left", "forearm_right",
        "thigh_left", "thigh_right", "calf_left", "calf_right"
    ]
    value: float

class GetCircumferenceHistoryRequest(BaseModel):
    user_id: int
    part: Literal[
        "neck", "shoulder", "chest", "waist", "hip",
        "arm_left", "arm_right", "forearm_left", "forearm_right",
        "thigh_left", "thigh_right", "calf_left", "calf_right"
    ]

class DeleteCircumferenceRecordRequest(BaseModel):
    user_id: int
    part: Literal[
        "neck", "shoulder", "chest", "waist", "hip",
        "arm_left", "arm_right", "forearm_left", "forearm_right",
        "thigh_left", "thigh_right", "calf_left", "calf_right"
    ]
    date: date