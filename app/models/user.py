from datetime import datetime

from sqlalchemy import TIMESTAMP, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Boolean

from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    profile = Column(Text, nullable=False)
    disabled = Column(Boolean, nullable=False)
