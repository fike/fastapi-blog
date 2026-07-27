from typing import Any

from pydantic import AnyUrl
from pydantic_settings import BaseSettings
from starlette.config import Config


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URI: AnyUrl | None = None
    SECRET_KEY: str | None = None
    ORIGINS: str | None = None
    TEST_SQLALCHEMY_DATABASE_URI: AnyUrl | None = None

    model_config = {"env_file": ".env"}


settings: Any = Settings()
config: str = Config(".env")
