from slugify import slugify
from sqlalchemy.orm import Session

from app import models, schemas


def create_post(db: Session, post: schemas.PostCreate):
    post_data = post.dict()
    post_data["slug"] = slugify(post_data["title"])
    db_post = models.Post(**post_data)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def get_post(db: Session, slug: str):
    post = db.query(models.Post).filter(models.Post.slug == slug).first()
    return post


def get_all(
    db: Session,
) -> list:
    posts = db.query(models.Post)
    return posts


def count_posts(db: Session) -> int:
    total = db.query(models.Post).count()
    return total
