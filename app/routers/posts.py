from typing import Any, Optional

from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi_pagination import Page, pagination_params
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session
from starlette.status import HTTP_201_CREATED

from app import schemas
from app.db.session import SessionLocal
from app.schemas import PostCreate
from app.services import (
    count_posts,
    create_post,
    get_all_posts,
    get_current_active_user,
    get_db,
    get_post,
    get_post_by_userid,
    get_user_by_id,
)

router = APIRouter(
    tags=["posts"],
    responses={404: {"Description": "Not found"}},
)


@router.post("/posts", response_model=schemas.Post, status_code=HTTP_201_CREATED)
def create_user_post(
    post: PostCreate, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_active_user)
):
    result = create_post(db=db, post=post, current_user=current_user)
    return result


@router.get("/posts/{slug}", response_model=schemas.Posts)
def read_slug(slug: str, db: Session = Depends(get_db)):
    db_slug = get_post(db, slug=slug)
    if db_slug is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_slug


@router.get("/posts", response_model=Page[schemas.Posts], dependencies=[Depends(pagination_params)])
def list_posts(response: Response, db: Session = Depends(get_db), user_id: Optional[int] = None) -> Any:
    db_user = ""
    if user_id:
        db_user = get_user_by_id(db=db, user_id=user_id)
        if db_user:
            posts = get_post_by_userid(db=db, user_id=user_id)
    else:
        posts = get_all_posts(db=db)

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    total_posts = count_posts(db=db)
    response.headers["X-Total-Posts"] = str(total_posts)

    return paginate(posts)
