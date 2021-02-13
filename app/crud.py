from sqlalchemy.orm import Session
from . import models, schemas


def create_post(db: Session, post: schemas.PostCreate):
    db_post = models.Post(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def get_all(
    db: Session,  # offset: int = 0, limit: int = 100
) -> list:
    posts = db.query(models.Post)
    return posts


def count_posts(
    db: Session
) -> int:
    total = db.query(models.Post).count()
    return total
