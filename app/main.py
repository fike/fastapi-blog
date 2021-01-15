from typing import Any, List

from fastapi import Depends, FastAPI, status
from sqlalchemy.orm import Session
from starlette.status import HTTP_201_CREATED

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Async FastAPI")

# logger = logging.getLogger("uvicorn.error")

# Dependency
def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()


# @app.post("/posts/", response_model=schemas.Post)
# def create_post(post = schemas.PostCreate, db: Session = Depends(get_db)):
#     return crud.create_post(db, post=post)

@app.post("/posts/", response_model=schemas.Post, status_code=HTTP_201_CREATED, tags=["posts"])
def create_post(
    post: schemas.PostCreate, db: Session = Depends(get_db)
):
    result =  crud.create_post(db=db, post=post)
    return result

