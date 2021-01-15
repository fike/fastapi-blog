from sqlalchemy import Integer, String
from sqlalchemy.sql.schema import Column, Index

from .database import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)

