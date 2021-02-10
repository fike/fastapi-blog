from typing import Any, List

from fastapi import Depends, FastAPI, Response
from sqlalchemy.orm import Session
from starlette.status import HTTP_201_CREATED

from opentelemetry import trace
from opentelemetry.exporter import jaeger
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchExportSpanProcessor
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor

from . import crud, schemas, models

from .db.session import SessionLocal, engine

trace.set_tracer_provider(TracerProvider())
trace_exporter = jaeger.JaegerSpanExporter(
    service_name="fastapi-blog",
    agent_host_name="jaeger-server",
    agent_port=6831,
)
trace.get_tracer_provider().add_span_processor(
    BatchExportSpanProcessor(trace_exporter)
)



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

@app.post("/posts/", response_model=schemas.Post, status_code=HTTP_201_CREATED, tags=["posts"])
def create_post(
    post: schemas.PostCreate, db: Session = Depends(get_db)
):
    result =  crud.create_post(db=db, post=post)
    return result

# TODO: pagination 
@app.get("/posts/", response_model=List[schemas.Post], tags=["posts"])
def list_posts(response: Response, db: Session = Depends(get_db), offset: int = 0, limit: int = 30) -> Any:
    posts = crud.get_all(db=db, offset=offset, limit=limit)
    total_posts = crud.count_posts(db=db)
    response.headers["X-Total-Posts"] = str(total_posts)

    return posts


FastAPIInstrumentor.instrument_app(app)
SQLAlchemyInstrumentor().instrument(engine=engine)