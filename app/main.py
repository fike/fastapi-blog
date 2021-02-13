from typing import Any

from fastapi import Depends, FastAPI, Response
from fastapi_pagination import Page, pagination_params
from fastapi_pagination.ext.sqlalchemy import paginate
from opentelemetry import trace
from opentelemetry.exporter import jaeger
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchExportSpanProcessor
from sqlalchemy.orm import Session
from starlette.status import HTTP_201_CREATED

from . import crud, models, schemas
from .db.session import SessionLocal, engine
from .schemas import PostCreate  # ListPostsResponse

trace.set_tracer_provider(TracerProvider())
trace_exporter = jaeger.JaegerSpanExporter(
    service_name="fastapi-blog",
    agent_host_name="jaeger-server",
    agent_port=6831,
)
trace.get_tracer_provider().add_span_processor(BatchExportSpanProcessor(trace_exporter))


# Create database tables to start
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Blog Backend")

# logger = logging.getLogger("uvicorn.error")

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/posts/", response_model=schemas.Post, status_code=HTTP_201_CREATED)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    result = crud.create_post(db=db, post=post)
    return result


@app.get("/posts/", response_model=Page[schemas.Posts], dependencies=[Depends(pagination_params)])
def list_posts(response: Response, db: Session = Depends(get_db)) -> Any:
    posts = crud.get_all(db=db)
    total_posts = crud.count_posts(db=db)
    response.headers["X-Total-Posts"] = str(total_posts)

    return paginate(posts)


FastAPIInstrumentor.instrument_app(app)
SQLAlchemyInstrumentor().instrument(engine=engine)
