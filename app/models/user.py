from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Boolean

from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True)
    username: str = Column(String(50), unique=True)
    email: str = Column(String, nullable=False)
    hashed_password: str = Column(String, nullable=False)
    profile: str = Column(Text, nullable=False)
    disabled: bool = Column(Boolean, nullable=False)
