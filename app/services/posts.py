from typing import Any

from slugify import slugify
from sqlalchemy.orm import Session

from app import models, schemas


def create_post(
    db: Session, post: schemas.PostCreate, current_user: schemas.User
) -> Any:
    post_data = post.dict()
    post_data["slug"] = slugify(post_data["title"])
    user_data = schemas.User.from_orm(current_user).dict()
    post_data["author_id"] = user_data["id"]
    db_post = models.Post(**post_data)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def get_post(db: Session, slug: str) -> Any:
    post = db.query(models.Post).filter(models.Post.slug == slug).first()
    return post


def get_all_posts(
    db: Session,
) -> list:
    posts = db.query(models.Post)
    return posts


def get_posts_by_userid(db: Session, user_id: int) -> list:
    return db.query(models.Post).filter(models.Post.author_id == user_id)


def count_posts(db: Session) -> int:
    total = db.query(models.Post).count()
    return total


def update_post(db: Session, post: str, slug: str) -> Any:
    db_post = get_post(db, slug)
    post_data: dict = post.dict()
    setattr(db_post, "title", post_data["title"])
    setattr(db_post, "slug", slugify(post_data["title"]))
    setattr(db_post, "body", post_data["body"])

    db.commit()
    db.refresh(db_post)
    return db_post


def delete_post(db: Session, slug: str) -> Any:
    db_post = get_post(db=db, slug=slug)
    db.delete(db_post)
    db.commit()
    return None
