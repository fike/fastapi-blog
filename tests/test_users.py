from datetime import timedelta

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.services.security import create_access_token

client = TestClient(app)


@pytest.mark.parametrize(
    ("username", "profile", "email", "disabled", "password", "status"),
    (
        ("leodoe", "Leo Doe Profile", "leodoe@test.org", False, "leodoepass", 201),
        ("annedoe", "Anne Doe Profile", "annedoe@test.org", True, "annedoepass", 201),
        ("bruce", "Bruce Doe Profile", "", True, "annedoepass", 422),
        ("jenny", "", "jennydoe@test.org", True, "jennydoepass", 422),
        ("tessdoe", "Tess Doe Profile", "tessdoe@test.org", False, "tessdoepass", 201),
        ("rossdoe", "Ross Doe Profile", "leodoe@test.org", False, "tessdoepass", 400),
        ("leodoe", "Mark Doe Profile", "markdow@test.org", False, "markdoepass", 400),
        ("a", "A user profile Profile", "a@test.org", False, "apass", 422),
    ),
)
def test_create_user(username, profile, email, disabled, password, status, request):
    response = client.post(
        "/users",
        json={"username": username, "profile": profile, "email": email, "disabled": disabled, "password": password},
    )
    assert status == response.status_code


@pytest.mark.parametrize(
    ("username", "password", "status"),
    (
        ("leodoe", "leodoepass", 200),
        ("leodoe", "leodoepassfailed", 401),
    ),
)
def test_get_token(username, password, status):
    data = {"username": username, "password": password}
    response = client.post("/token", data=data)
    assert status == response.status_code


def test_get_users():
    response = client.get("/users")
    assert 200 == response.status_code


@pytest.mark.parametrize(
    ("username", "user_id", "status"),
    (
        ("annedoe", "", 200),
        ("wronguser", "", 404),
        ("", "1", 200),
        ("", "200", 404),
        ("", "", 404),
    ),
)
def test_get_user(username, user_id, status):
    if username:
        response = client.get("/users/user?username=" + username)
    elif user_id:
        response = client.get("/users/user?user_id=" + user_id)
    else:
        response = client.get("/users/user")
    assert status == response.status_code


@pytest.mark.parametrize(
    ("username", "status"),
    (
        ("leodoe", 200),
        ("", 401),
        ("annedoe", 401),
    ),
)
def test_posts_by_user(username, status):
    headers = {}
    req_time = timedelta(minutes=30)
    data = {"sub": username}
    token_data = create_access_token(data=data, expires_delta=req_time)
    headers["Authorization"] = "Bearer " + token_data
    response = client.get("/users/me/posts", headers=headers)
    assert status == response.status_code
