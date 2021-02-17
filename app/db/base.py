from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr

from .session import SessionLocal


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# It's used to create tables "normalized".
# Future apply to inflect from models to plural tables name.


@as_declarative()
class Base:
    id: Any
    __name__: str
