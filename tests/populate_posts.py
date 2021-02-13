#!/usr/bin/env python

import json

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
trace.get_tracer_provider().add_span_processor(BatchExportSpanProcessor(trace_exporter))

RequestsInstrumentor().instrument()

post_template = dict({"title": "Title Foo", "body": "Body foobar"})

url = "http://localhost:8000/posts/"


for i in range(1, 300):
    headers = {}
    post_title = str(post_template["title"] + str(i))
    post_body = str(post_template["body"] + str(i))
    post_req = json.dumps(dict({"title": post_title, "body": post_body}))
    resp = requests.post(url, data=post_req, headers=headers)
    print(resp.text)

    assert resp.status_code == 201
