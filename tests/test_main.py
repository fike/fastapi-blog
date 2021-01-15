import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base, SessionLocal, engine
from app.main import app

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)



client = TestClient(app)

@pytest.mark.parametrize(
    ("title_header", "title_body", "status"),
    (
        ("title", "Test title blog 1", 201),
        ("titl1", "Test title blog 2", 422),
        ("title", "", 422),
        ("", "Test title blog 3", 422),
    )
)
def test_create_post(title_header, title_body, status):
    response = client.post(
        "/posts/",
        json={title_header: title_body},
    )
    print(response.text)
    # data = response.json()
    # assert data["title"] == "Test title blog"
    assert status == response.status_code