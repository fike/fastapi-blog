from os import environ
from typing import Any

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.routers import users

from .db.session import engine
from .routers import posts

# Create database tables to start
# models.Base.metadata.create_all(bind=engine)

app: Any = FastAPI(title="FastAPI Blog Backend - Opentelemetry, Jaeger")

# logger = logging.getLogger("uvicorn.error")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


otel_trace: Any = environ.get("OTELE_TRACE")

if otel_trace == "True":  # pragma: no cover
    from opentelemetry import trace
    from opentelemetry.exporter import jaeger
    from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import (
        OTLPSpanExporter,
    )
    from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
    from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor
    from opentelemetry.sdk.resources import Resource

    # from opentelemetry.instrumentation.psycopg2 import Psycopg2Instrumentor
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import BatchSpanProcessor

    resource = Resource(attributes={"service.name": "fastapi-blog"})
    trace.set_tracer_provider(TracerProvider(resource=resource))
    tracer = trace.get_tracer(__name__)

    otlp_exporter = OTLPSpanExporter(
        endpoint="otel-collector:4317", insecure=True
    )

    span_processor = BatchSpanProcessor(otlp_exporter)

    trace.get_tracer_provider().add_span_processor(span_processor)

    FastAPIInstrumentor.instrument_app(app)

    SQLAlchemyInstrumentor().instrument(engine=engine)
else:
    pass

app.include_router(posts.router)
app.include_router(users.router)
