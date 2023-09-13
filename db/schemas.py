from datetime import datetime
from typing import Optional

from pydantic import BaseModel as PydenticBaseModel


class BaseModel(PydenticBaseModel):
    class Config:
        orm_mode = True


class ResponseBaseModel(BaseModel):
    id: Optional[int]
    creation_date: Optional[datetime]
    update_date: Optional[datetime]
    created_by: Optional[int]
    updated_by: Optional[int]
