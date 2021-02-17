from os import environ
from typing import Any

from fastapi import FastAPI
from starlette.status import HTTP_201_CREATED

from . import models
from .db.session import engine
from .routers import posts

# Create database tables to start
models.Base.metadata.create_all(bind=engine)


app = FastAPI(title="FastAPI Blog Backend")

# logger = logging.getLogger("uvicorn.error")

otel_trace = environ.get("OTELE_TRACE")

if otel_trace == "True":  # pragma: no cover
    from opentelemetry import trace
    from opentelemetry.exporter import jaeger
    from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
    from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import BatchExportSpanProcessor

    trace.set_tracer_provider(TracerProvider())
    trace_exporter = jaeger.JaegerSpanExporter(
        service_name="fastapi-blog",
        agent_host_name="jaeger-server",
        agent_port=6831,
    )
    trace.get_tracer_provider().add_span_processor(BatchExportSpanProcessor(trace_exporter))
    FastAPIInstrumentor.instrument_app(app)
    SQLAlchemyInstrumentor().instrument(engine=engine)
else:
    pass


app.include_router(posts.router, prefix="/api")
