from sqlalchemy import Integer, String
from sqlalchemy.sql.schema import Column, Index

from .db.base import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), index=True, nullable=False)
    body = Column(String, index=False, nullable=False)
