from datetime import datetime

import sqlalchemy
from sqlalchemy import TIMESTAMP, Integer, String, Text
from sqlalchemy.sql.schema import Column, ForeignKey

from .db.base import Base

# from sqlalchemy.sql.sqltypes import DateTime


# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True)
#     username = Column(String(50), unique=True)
#     password = Column(String, nullable=False)
#     profile = Column(Text, nullable=False)


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    # author_id = Column(ForeignKey(User.id), nullable=False)
    slug = Column(String, index=True)
    title = Column(String(100), index=True, nullable=False)
    body = Column(String, index=False, nullable=False)
    published = Column(TIMESTAMP(timezone=True), default=datetime.now)
