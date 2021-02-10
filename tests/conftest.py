from typing import Generator
import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.main import get_db
from app.config import settings
from app.db.session import SessionLocal
from app.main import app
from app.models import Post


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




# from _pytest.monkeypatch import monkeypatch
# import pytest
# from fastapi.testclient import TestClient

# from app.main import app

# @pytest.fixture(scope="module")
# def test_app():
#     client = TestClient(app)
#     yield client



# user = monkeypatch.setenv("POSTGRES_USER", "test")
# password = monkeypatch.setenv("POSTGRES_PASSWORD", "test")
# db = monkeypatch.setenv("POSTGRES_DB", "test")
# SQL_ALCHEMY_DATABASE_URI = f"postgresql://{user}:{password}@{server}/{db}"


# @pytest.fixture()
# def test_conn():
# # @pytest.fixture
# # def mock_test_conn():
#     server = monkeypatch.setenv("POSTGRES_SERVER", "localhost")
#     user = monkeypatch.setenv("POSTGRES_USER", "test")
#     password = monkeypatch.setenv("POSTGRES_PASSWORD", "test")
#     db = monkeypatch.setenv("POSTGRES_DB", "test")
#     SQL_ALCHEMY_DATABASE_URI = f"postgresql://{user}:{password}@{server}/{db}"


#     assert SQL_ALCHEMY_DATABASE_URI == "postgresql://test:test@localhost/test"
