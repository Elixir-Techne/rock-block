import logging
import uuid
from contextvars import ContextVar

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.routing import Match

from apps.integration.api.v1 import router
from rockblock_integration.core.config import settings
from rockblock_integration.core.logs import setup_logging

logger = logging.getLogger(__name__)


def get_application():
    _app = FastAPI(
        title=settings.PROJECT_NAME,
        docs_url="/",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
        version="1.0.0",
        debug=settings.DEBUG
    )

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app


app = get_application()
request_id_contextvar = ContextVar("request_id", default=None)


@app.middleware("http")
async def request_middleware(request, call_next):
    request_id = str(uuid.uuid4())
    request_url = str(request.url)
    request_id_contextvar.set(request_id)
    request_method = request.method
    logger.info(f"Request started, Method:{request_method}, URL: {request_url}")
    routes = request.app.router.routes
    logger.debug("Request Params:")
    for route in routes:
        match, scope = route.matches(request)
        if match == Match.FULL:
            for name, value in scope["path_params"].items():
                logger.debug(f"\t{name}: {value}")
    logger.debug("Request Headers:")
    for name, value in request.headers.items():
        logger.debug(f"\t{name}: {value}")

    try:
        return await call_next(request)
    except Exception as ex:
        logger.error(f"Request failed: {ex}")
        raise
    finally:
        logger.info(f"Request Ended, Method:{request_method}, URL: {request_url}")


@app.on_event("startup")
async def startup_event():
    setup_logging()


app.include_router(router)
