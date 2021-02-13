import pytest
from _pytest.monkeypatch import monkeypatch
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db.base import Base
from app.db.session import engine
from app.main import app, get_db

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


client = TestClient(app)


@pytest.mark.parametrize(
    ("title_header", "title_value", "body_header", "body_value", "status"),
    (
        ("title", "Test title blog 1", "body", "Test body blog 1", 201),
        ("titl1", "Test title blog 2", "body", "Test body blog 2", 422),
        ("title", "", "body", "Test body blog3", 422),
        ("", "Test title blog 3", "body", "Test body blog 4", 422),
        (
            "title",
            "Test title - 1231453klfdncas\vnfaotg243rq34jfrngvkjsdfnlskedfasnbgkdndksfjaio32wrj34bn5kl34nfakdnsfakds",
            "body",
            "Test body blog5",
            422,
        ),
        ("title", "Test title blog 4", "", "Test body blog 6", 422),
        ("title", "Test title blog 5", "body1", "Test body blog 7", 422),
        ("title", "Test title blog 6", "body", "", 422),
    ),
)
def test_create_post(title_header, title_value, body_header, body_value, status):
    response = client.post(
        "/posts/",
        json={title_header: title_value, body_header: body_value},
    )
    assert status == response.status_code


def test_get_post():
    response = client.get("/posts/")
    assert 200 == response.status_code
