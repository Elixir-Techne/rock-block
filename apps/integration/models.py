from sqlalchemy import Column, String, TIMESTAMP, Float, Integer

from db import Base


class Integration(Base):
    imei = Column(String)
    data = Column(String)

