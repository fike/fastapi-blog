from typing import Any

from sqlalchemy.orm import Session

from app import models, schemas

from . import security


def get_user_by_email(db: Session, email: str) -> Any:
    return db.query(models.User).filter(models.User.email == email).first()


def get_user_by_id(db: Session, user_id: int) -> Any:
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(db: Session, username: str) -> Any:
    return (
        db.query(models.User).filter(models.User.username == username).first()
    )


def get_users(db: Session):
    return db.query(models.User)


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = security.get_hash_password(user.password)
    user_data = user.model_dump()
    del user_data["password"]
    user_data["hashed_password"] = hashed_password
    user_post = models.User(**user_data)
    db.add(user_post)
    db.commit()
    db.refresh(user_post)
    return user_post


def update_user(db: Session, user: schemas.UserUpdate, username: str):
    db_user = get_user_by_username(db=db, username=username)
    user_data = user.model_dump()
    new_password = user_data.get("password")
    if new_password:
        password = security.get_hash_password(user_data["password"])
        db_user.hashed_password = password
    db_user.username = user_data["username"]
    db_user.profile = user_data["profile"]
    db_user.email = user_data["email"]
    db_user.disabled = user_data["disabled"]

    db.commit()
    db.refresh(db_user)
    return db_user
