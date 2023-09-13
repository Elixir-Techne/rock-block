from datetime import datetime

from db.schemas import ResponseBaseModel, BaseModel


class IntegrationCreateSchema(BaseModel):
    imei: str
    data: str


class IntegrationSchema(ResponseBaseModel):
    imei: str
    data: str
