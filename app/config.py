from typing import Any, Optional

from pydantic import PostgresDsn
from pydantic.env_settings import BaseSettings
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn]


settings: Any = Settings()

config: str = Config(".env")

# to get a string like this run:
# openssl rand -hex 32 and store to .env file
SECRET_KEY: str = config("SECRET_KEY")
