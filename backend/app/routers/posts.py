from http import HTTPStatus
from typing import Any, Optional

from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi_pagination import Page, pagination_params
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from app import schemas
from app.services import (
    count_posts,
    create_post,
    delete_post,
    get_all_posts,
    get_current_active_user,
    get_db,
    get_post,
    get_posts_by_userid,
    get_user_by_id,
)
from app.services.posts import update_post

router: Any = APIRouter(
    tags=["posts"],
    responses={404: {"Description": "Not found"}},
)


@router.post(
    "/posts",
    response_model=schemas.PostInDB,
    status_code=status.HTTP_201_CREATED,
)
def create_user_post(
    post: schemas.PostCreate,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_active_user),
) -> Any:
    """
    Create a post, needs the user is logged
    """
    result = create_post(db=db, post=post, current_user=current_user)
    return result


@router.get("/posts/{slug}", response_model=schemas.Posts)
def read_slug(slug: str, db: Session = Depends(get_db)) -> Any:
    """
    Get a post by slug
    """
    db_slug = get_post(db, slug)
    if db_slug is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_slug


@router.get(
    "/posts",
    response_model=Page[schemas.Posts],
    dependencies=[Depends(pagination_params)],
)
def list_posts(
    response: Response,
    db: Session = Depends(get_db),
    user_id: Optional[int] = None,
) -> Any:
    """
    List all post published
    """
    db_user = ""
    if user_id:
        db_user = get_user_by_id(db=db, user_id=user_id)
        print(db_user)
        if db_user:
            posts = get_posts_by_userid(db=db, user_id=user_id)
    else:
        posts = get_all_posts(db=db)

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    total_posts = count_posts(db=db)
    response.headers["X-Total-Posts"] = str(total_posts)

    return paginate(posts)


@router.put("/posts/{slug}", response_model=schemas.PostInDB)
def update_user_post(
    slug: str,
    post: schemas.PostCreate,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_active_user),
) -> Any:
    """
    Update a user Post if its owner
    """
    post_data = get_post(db, slug)
    if post_data is None:
        raise HTTPException(status_code=404, detail="Don't find post")
    elif post_data.author_id != current_user.id:
        raise HTTPException(status_code=403, detail="Don't have permission")
    req_post = update_post(db=db, slug=slug, post=post)
    return req_post


@router.delete("/posts/{slug}", status_code=HTTPStatus.NO_CONTENT)
def post_delete(
    slug: str,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_user),
) -> Any:
    """
    Delete a user post if its owner
    """
    post_data = get_post(db, slug)
    if post_data is None:
        raise HTTPException(status_code=404, detail="Post not found")
    if post_data.author_id != current_user.id:
        raise HTTPException(status_code=403, detail="Don't have permission")
    delete_post(db, slug)
    return Response(status_code=HTTPStatus.NO_CONTENT.value)
