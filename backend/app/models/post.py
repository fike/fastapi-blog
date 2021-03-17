from datetime import datetime

from sqlalchemy import TIMESTAMP, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column, ForeignKey

from app.db.base import Base

from . import user


class Post(Base):
    __tablename__: str = "posts"

    id: int = Column(Integer, primary_key=True, index=True)
    author_id: int = Column(ForeignKey(user.User.id), nullable=False)
    slug: str = Column(String, index=True)
    title: str = Column(String(100), index=True, nullable=False)
    summary: str = Column(String(240), index=False, nullable=False)
    body: str = Column(String, index=False, nullable=False)
    published_at: datetime = Column(
        TIMESTAMP(timezone=True), default=datetime.now()
    )
