from typing import Any, Optional

from pydantic import PostgresDsn
from pydantic.env_settings import BaseSettings
from starlette.config import Config


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn]
    SECRET_KEY: Optional[str]
    ORIGINS: Optional[str]
    TEST_SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn]

    class Config:
        env_file = ".env"


settings: Any = Settings()
config: str = Config(".env")
