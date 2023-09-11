import logging
from typing import List

from fastapi import APIRouter, Depends, Query
from sqlalchemy import Date, desc
from sqlalchemy.orm import Session
from datetime import datetime
from apps.integration.models import Integration
from apps.integration.schemas import IntegrationSchema
from db.dependencies import get_db

router = APIRouter(
    tags=["Integration"],
    prefix="/integration"
)

logger = logging.getLogger(__name__)


@router.post("/", response_model=IntegrationSchema)
def create_integrations(payload: dict, db: Session = Depends(get_db), ):
    logger.info("Integration create API called with data: %s", payload)
    print(payload)
    transmit_time = payload.get("transmit_time")
    if transmit_time:
        transmit_time = datetime.strptime(transmit_time, '%y-%m-%d %H:%M:%S')
    integration_instance = Integration(
        imei=payload.get("imei"),
        serial=payload.get("serial"),
        momsn=payload.get("momsn"),
        transmit_time=transmit_time,
        iridium_latitude=payload.get("iridium_latitude"),
        iridium_longitude=payload.get("iridium_longitude"),
        iridium_cep=payload.get("iridium_cep"),
        data=payload.get("data"),
        JWT=payload.get("JWT"),
        device_type=payload.get("device_type"),
    )
    db.add(integration_instance)
    db.commit()
    db.refresh(integration_instance)
    logger.info("Integration created successfully")
    return integration_instance


@router.get("/", response_model=List[IntegrationSchema])
def get_integrations(
        offset: int = 0,
        limit: int = Query(default=10),
        db: Session = Depends(get_db),
        imei: str = Query(""),
        device_type: str = Query(""),
        transmit_time: str = Query(""),
        start_date: str = Query(""),
        end_date: str = Query("")
):
    logger.info("Integration get API called")
    integrations = db.query(Integration)
    if imei:
        integrations = integrations.filter(Integration.imei == imei)
    if device_type:
        integrations = integrations.filter(Integration.device_type == device_type)
    if transmit_time:
        integrations = integrations.filter(Integration.transmit_time == transmit_time)
    if start_date and end_date:
        integrations = integrations.filter(
            Integration.creation_date.cast(Date) >= start_date,
            Integration.creation_date.cast(Date) <= end_date
        )
    logger.info("Integration data fetched successfully")
    return integrations.order_by(desc(Integration.id)).limit(limit).offset(offset).all()
