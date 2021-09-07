import json
from datetime import timedelta

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.services.security import create_access_token

client = TestClient(app)


long_title = (
    "Test title - "
    "1231453klfdncas\vnfaotg243rq34jfrngvkjsdfnls"
    "kedfasnbgkdndksfjaio32wrj34bn5kl34nfakdnsfakds"
)
long_summary = (
    "a egeanbv t qvfdagasdfoghed erogfvedimvgadfgadfag"
    "fasd fgaovrmehyynnmsdf  adfgasdfgadsogagberthetrh"
    "adf asdf aspertabvgnhbgn  nhnjmhjhnmbv nvcwrerehg"
    "f fdgvsdhtnbnmnýtqworeuwiyt    reyw qreptoieryhutrw"
    "afsdf awrtqwfwghhth  tuhytpojfghnj mvbnm2353546cvvs"
)


@pytest.mark.order(-2)
@pytest.mark.parametrize(
    ("username", "title", "summary", "body", "status"),
    (
        (
            "leodoe",
            "Leo title blog1",
            "Leo summary post 1",
            "Leo body post blog1",
            201,
        ),
        ("leodoe", "", "Leo summary post 1", "Leo body post blog1", 422),
        ("leodoe", "Leo title blog1", "", "Leo body post blog1", 422),
        ("leodoe", "Leo title blog1", "Leo summary post 1", "", 422),
        (
            "leodoe",
            long_title,
            "Leo summary post 1",
            "Leo long title exploit",
            422,
        ),
        (
            "leodoe",
            "Leo long summary exploit",
            long_summary,
            "Leo long title exploit",
            422,
        ),
        (
            "tessdoe",
            "Tess title blog 2",
            "Tess summary post 2",
            "Tess body post blog 2",
            201,
        ),
        (
            "tessdoe",
            "Tess title blog 3",
            "Tess summary post 3",
            "Tess body post blog 3",
            201,
        ),
    ),
)
def test_create_post(username, title, summary, body, status):
    headers = {}
    req_time = timedelta(minutes=30)
    data = {"sub": username}
    token_data = create_access_token(data=data, expires_delta=req_time)
    headers["Authorization"] = "Bearer " + token_data
    response = client.post(
        "/posts",
        json={"title": title, "summary": summary, "body": body},
        headers=headers,
    )
    assert status == response.status_code


@pytest.mark.order(-2)
def test_get_posts():
    response = client.get("/posts")
    data = json.loads(response.text)
    assert 200 == response.status_code
    assert data["items"][0]["published_at"] != data["items"][1]["published_at"]


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


@pytest.mark.order(-2)
@pytest.mark.parametrize(
    ("username", "slug", "title", "summary", "body", "status"),
    (
        (
            "tessdoe",
            "tess-title-blog-2",
            "Tess title blog 2",
            "Tess summary post 2 - modified",
            "Tess body post blog 2 - Modified",
            200,
        ),
        (
            "tessdoe",
            "tess-title-not-found",
            "Tess title blog 2",
            "Tess summary post 2 - modified",
            "Tess body post blog 2 - Modified",
            404,
        ),
        (
            "leodoe",
            "tess-title-blog-2",
            "Tess title blog 3",
            "Tess summary post 3 - modified",
            "Tess body post blog 3 - Modified",
            403,
        ),
    ),
)
def test_update_post(username, slug, title, summary, body, status):
    headers = {}
    req_time = timedelta(minutes=30)
    data = {"sub": username}
    token_data = create_access_token(data=data, expires_delta=req_time)
    headers["Authorization"] = "Bearer " + token_data

    response = client.put(
        "/posts/" + slug,
        json={"title": title, "summary": summary, "body": body},
        headers=headers,
    )
    assert status == response.status_code


@pytest.mark.order(-1)
@pytest.mark.parametrize(
    ("username", "path", "slug", "status"),
    (
        ("tessdoe", "tess-title-blog-3", "tell-title-blog-3", 204),
        ("tessdoe", "tell-title-blog-10000", "tell-title-blog-3", 404),
        ("leodoe", "tess-title-blog-2", "tell-title-blog-2", 403),
    ),
)
def test_delete_post(username, path, slug, status):
    headers = {}
    req_time = timedelta(minutes=30)
    data = {"sub": username}
    token_data = create_access_token(data=data, expires_delta=req_time)
    headers["Authorization"] = "Bearer " + token_data
    response = client.delete("/posts/" + path, headers=headers)
    assert status == response.status_code
