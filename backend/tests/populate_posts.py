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

data_body_template = """

Lorem ipsum dolor sit amet, **consectetur** *adipiscing* elit. Phasellus
condimentum turpis non nisl pellentesque, ac lobortis metus viverra.
Quisque placerat quam dolor, sit amet semper tortor porttitor in.
Aenean ut ante eget ex suscipit mollis posuere vitae ante.
Pellentesque tristique sollicitudin orci, sit amet sagittis purus
pulvinar sed. Aliquam dictum dui vitae dolor sollicitudin, nec
venenatis lacus eleifend. Nam malesuada leo est, at sollicitudin enim
commodo et. Integer scelerisque a arcu quis condimentum. Nulla semper
sit amet dui vitae iaculis. Quisque nibh sem, bibendum vitae aliquam
quis, semper quis ligula. Maecenas luctus nunc ornare erat
condimentum, vitae condimentum lorem varius. Etiam mattis tellus
consequat urna vestibulum, nec egestas augue pretium.

```c:hello.c
#include <stdio.h>

int main(void)
{
    printf("hello, world");
}
```

Pellentesque mauris massa, [vulputate](http://localhost:3000) in quam
a, dignissim cursus ipsum. Donec non lacinia eros, non accumsan nunc.
Quisque quis varius arcu, eu suscipit diam. Interdum et malesuada
fames ac ante ipsum primis in faucibus. Fusce dolor neque, sodale
ut molestie ac, posuere ac enim. Sed id sapien ut odio dapibus finibus
at nec purus. Duis cursus facilisis vestibulum. Lorem ipsum dolor sit
amet, consectetur adipiscing elit. Morbi feugiat enim eget efficitur
interdum. """

data_summary_template = "A fake summary generate to test "

data_post_template = dict(
    {
        "title": "Title Foo",
        "summary": data_summary_template,
        "body": data_body_template,
    }
)

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
        post_summary = str(
            data_post_template["summary"]
            + " - "
            + i["username"]
            + " - "
            + date_txt.strftime("%Y/%m/%d - %H:%m:%S")
        )
        post_req = json.dumps(
            dict(
                {
                    "title": post_title,
                    "summary": post_summary,
                    "body": post_body,
                }
            )
        )
        resp = requests.post(url, data=post_req, headers=headers)
        print(resp.text)
        assert resp.status_code == 201

RequestsInstrumentor().instrument()
