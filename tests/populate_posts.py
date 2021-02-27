#!/usr/bin/env python

import json
import time
from datetime import datetime

import requests
from opentelemetry import trace
from opentelemetry.exporter import jaeger
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchExportSpanProcessor

trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer_provider().get_tracer(__name__)

trace_exporter = jaeger.JaegerSpanExporter(
    service_name="fastapi-blog-client",
    agent_host_name="localhost",
    agent_port=6831,
)
trace.get_tracer_provider().add_span_processor(
    BatchExportSpanProcessor(trace_exporter)
)


URLBASE = "http://localhost:8000/"

data_post_template = dict({"title": "Title Foo", "body": "Body foobar"})

data_user_template = [
    {
        "username": "florencedoe",
        "profile": "Florence Doe profile",
        "email": "florence@test.org",
        "disable": False,
        "password": "florencedoe",
    },
    {
        "username": "johndoe",
        "profile": "John Doe profile",
        "email": "john@test.org",
        "disable": False,
        "password": "johndoe",
    },
    {
        "username": "marydoe",
        "profile": "Mary Doe profile",
        "email": "mary@test.org",
        "disable": False,
        "password": "marydoe",
    },
]


def create_users():
    for i in data_user_template:
        headers = {}
        url = URLBASE + "users"
        data = json.dumps(i)
        result = requests.post(url, data=data, headers=headers)
        print(result.content)


def get_token(username, password):
    url = URLBASE + "token"
    headers = {}
    user_login = username
    user_pass = password
    data = {"username": user_login, "password": user_pass}
    result = requests.post(url, data=data, headers=headers)
    token_header = json.loads(result.content)
    return token_header["access_token"]


create_users()

for y in range(1, 100):
    for i in data_user_template:
        time.sleep(1)
        headers = {}
        date_txt = datetime.now()
        url = URLBASE + "posts"
        username = i["username"]
        password = i["password"]
        try:
            token = get_token(username, password)
        except Exception as e:
            print(e.args)
            continue
        headers["Authorization"] = "Bearer " + token
        post_title = str(
            data_post_template["title"]
            + " - "
            + i["username"]
            + " - "
            + date_txt.strftime("%Y/%m/%d - %H:%m:%S")
        )
        post_body = str(
            data_post_template["body"]
            + " - "
            + i["username"]
            + " - "
            + date_txt.strftime("%Y/%m/%d - %H:%m:%S")
        )
        post_req = json.dumps(dict({"title": post_title, "body": post_body}))
        resp = requests.post(url, data=post_req, headers=headers)
        print(resp.text)
        assert resp.status_code == 201

RequestsInstrumentor().instrument()
