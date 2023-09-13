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


@router.post("/")
def create_integrations(payload: dict, db: Session = Depends(get_db), ):
    logger.info("Integration create API called with data: %s", payload)
    integration_instance = Integration(
        imei=payload.get("imei"),
        data=payload.get("data"),
    )
    db.add(integration_instance)
    db.commit()
    db.refresh(integration_instance)
    logger.info("Integration created successfully")
    return "ok"


@router.get("/", response_model=List[IntegrationSchema])
def get_integrations(
        offset: int = 0,
        limit: int = Query(default=10),
        db: Session = Depends(get_db),
        imei: str = Query(""),
):
    logger.info("Integration get API called")
    integrations = db.query(Integration)
    if imei:
        integrations = integrations.filter(Integration.imei == imei)
    logger.info("Integration data fetched successfully")
    return integrations.order_by(desc(Integration.id)).limit(limit).offset(offset).all()
