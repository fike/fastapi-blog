from typing import Generator

import pytest
from fastapi.testclient import TestClient

# from app.config import settings
from app.db.session import SessionLocal
from app.main import app, get_db
from app.models import Post

# from sqlalchemy.orm import Session


@pytest.fixture(scope="session")
def db():
    yield SessionLocal()


@pytest.fixture()
def client(db) -> Generator:
    def override_get_db():
        return db

        app.dependency_overrides[get_db] = override_get_db

    try:
        yield TestClient(app)
    finally:
        db.query(Post).delete()
        db.commit()
