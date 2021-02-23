from datetime import datetime

from sqlalchemy import TIMESTAMP, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column, ForeignKey

from app.db.base import Base

from . import user


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    author_id = Column(ForeignKey(user.User.id), nullable=False)
    slug = Column(String, index=True)
    title = Column(String(100), index=True, nullable=False)
    body = Column(String, index=False, nullable=False)
    published = Column(TIMESTAMP(timezone=True), default=datetime.now)
