from typing import Any, Optional

from sqlalchemy.orm import Session

from app import models, schemas

from . import security


def get_user(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_users(db: Session) -> list:
    users = db.query(models.User)
    return users


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = security.get_hash_password(user.password)
    user_data = user.dict()
    user_data["password"] = hashed_password
    user_post = models.User(**user_data)
    db.add(user_post)
    db.commit()
    db.refresh(user_post)
    return user_post
