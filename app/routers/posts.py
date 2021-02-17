from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi_pagination import Page, pagination_params
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session
from starlette.status import HTTP_201_CREATED

from app.schemas import PostCreate

from .. import crud, schemas
from ..db.base import get_db
from ..db.session import SessionLocal

router = APIRouter(
    prefix="/posts",
    tags=["posts"],
    responses={404: {"Description": "Not found"}},
)


@router.post("", response_model=schemas.Post, status_code=HTTP_201_CREATED)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    result = crud.create_post(db=db, post=post)
    return result


@router.get("", response_model=Page[schemas.Posts], dependencies=[Depends(pagination_params)])
def list_posts(response: Response, db: Session = Depends(get_db)) -> Any:
    posts = crud.get_all(db=db)
    total_posts = crud.count_posts(db=db)
    response.headers["X-Total-Posts"] = str(total_posts)

    return paginate(posts)


@router.get("/{slug}", response_model=schemas.Post)
def read_slug(slug: str, db: Session = Depends(get_db)):
    db_slug = crud.get_post(db, slug=slug)
    if db_slug is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_slug
