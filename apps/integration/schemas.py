from datetime import datetime

from db.schemas import ResponseBaseModel, BaseModel


class IntegrationCreateSchema(BaseModel):
    imei: str
    serial: int
    momsn: int
    transmit_time: datetime
    iridium_latitude: float
    iridium_longitude: float
    iridium_cep: float
    data: str
    JWT: str
    device_type: str


class IntegrationSchema(ResponseBaseModel):
    imei: str
    serial: int
    momsn: int
    transmit_time: datetime
    iridium_latitude: float
    iridium_longitude: float
    iridium_cep: float
    data: str
    device_type: str
    JWT: str
