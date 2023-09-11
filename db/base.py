from sqlalchemy import Column, func, TIMESTAMP, Integer
from sqlalchemy.orm import declared_attr, as_declarative


@as_declarative()
class Base:
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    creation_date = Column(TIMESTAMP(timezone=True), server_default=func.now())
    update_date = Column(TIMESTAMP(timezone=True), onupdate=func.now())
    created_by = Column(Integer, nullable=True)
    updated_by = Column(Integer, nullable=True)

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
