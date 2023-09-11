from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from starlette.testclient import TestClient

from db import Base
from db.dependencies import get_db
from rockblock_integration.core.config import settings
from rockblock_integration.main import app

if settings.TEST_DATABASE_URL == "sqlite:///./test_db.db":
    engine = create_engine(
        settings.TEST_DATABASE_URL, echo=True, connect_args={'check_same_thread': False}
    )
else:
    engine = create_engine(settings.TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)
