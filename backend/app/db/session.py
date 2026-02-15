from typing import Any

from sqlalchemy import create_engine, engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import settings

engine = create_engine(  # noqa
    str(settings.SQLALCHEMY_DATABASE_URI), pool_pre_ping=True
)
SessionLocal: Any = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

Base: Any = declarative_base()
