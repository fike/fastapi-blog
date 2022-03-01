from typing import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker

from app.config import settings
from app.db.base import Base
from app.db.session import SessionLocal
from app.main import app

engine = create_engine(  # noqa
    settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True
)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)
Base.metadata.create_all(bind=engine)


@pytest.fixture(scope="function")
def db():
    yield SessionLocal()


@pytest.fixture(scope="function")
def client(db) -> Generator:
    try:
        TestClient(app)
        yield TestClient(app)
    finally:
        db.close()
