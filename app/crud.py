from sqlalchemy.orm import Session
from . import models, schemas

def create_post(db: Session, post: schemas.PostCreate):
    db_post = models.Post(**post.dict())
    print(db_post)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post
    