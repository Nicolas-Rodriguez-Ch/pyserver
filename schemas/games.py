from pydantic import BaseModel
from datetime import datetime


class GameCreate(BaseModel):
    map: str
    role: str
    mode: str
    outcome: str


class GameResponse(BaseModel):
    id: int
    map: str
    role: str
    mode: str
    outcome: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
