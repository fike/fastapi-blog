import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.services.security import authenticate_user, create_access_token

client = TestClient(app)


def test_auth_user(db):
    res = authenticate_user(db, "leodoe1", "leodoepass")
    assert res is False


def test_create_access_token():
    data = {"sub": "johndoe"}
    expire_delta = ""
    result = create_access_token(data, expire_delta)
    assert result is not None
