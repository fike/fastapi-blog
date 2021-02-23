from datetime import timedelta

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.services.security import create_access_token

client = TestClient(app)


long_title = "Test title - 1231453klfdncas\vnfaotg243rq34jfrngvkjsdfnlskedfasnbgkdndksfjaio32wrj34bn5kl34nfakdnsfakds"


@pytest.mark.order(-2)
@pytest.mark.parametrize(
    ("username", "title", "body", "status"),
    (
        ("leodoe", "Leo title blog1", "Leo body post blog1", 201),
        ("leodoe", "", "Leo body post blog1", 422),
        ("leodoe", "Leo title blog1", "", 422),
        ("leodoe", long_title, "Leo long title exploit", 422),
    ),
)
def test_create_post(username, title, body, status):
    headers = {}
    req_time = timedelta(minutes=30)
    data = {"sub": username}
    token_data = create_access_token(data=data, expires_delta=req_time)
    headers["Authorization"] = "Bearer " + token_data
    response = client.post("/posts", json={"title": title, "body": body}, headers=headers)
    assert status == response.status_code


def test_get_posts():
    response = client.get("/posts")
    assert 200 == response.status_code


@pytest.mark.order(-1)
@pytest.mark.parametrize(
    ("user_id", "status"),
    (
        ("1", 200),
        ("20", 404),
        ("", 200),
    ),
)
def test_get_users_posts(user_id, status):
    if user_id:
        response = client.get("/posts?user_id=" + str(user_id))
    else:
        response = client.get("/posts")
    assert status == response.status_code


@pytest.mark.order(-1)
@pytest.mark.parametrize(
    ("slug", "status"),
    (
        ("leo-title-blog1", 200),
        ("leo-body-post-blog-error", 404),
    ),
)
def test_get_post(slug, status):
    response = client.get(f"/posts/{slug}")
    assert status == response.status_code
