from sqlalchemy import Column, String, TIMESTAMP, Float, Integer

from db import Base


class Integration(Base):
    imei = Column(String)
    serial = Column(Integer)
    momsn = Column(Integer)
    transmit_time = Column(TIMESTAMP(timezone=True), nullable=True)
    iridium_latitude = Column(Float)
    iridium_longitude = Column(Float)
    iridium_cep = Column(Float)
    data = Column(String)
    JWT = Column(String)
    device_type = Column(String)
