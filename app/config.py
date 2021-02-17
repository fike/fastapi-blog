from typing import Optional

from pydantic import PostgresDsn
from pydantic.env_settings import BaseSettings


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn]


settings = Settings()
