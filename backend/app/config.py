from typing import Any, Optional

from pydantic import AnyUrl
from pydantic_settings import BaseSettings
from starlette.config import Config


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URI: Optional[AnyUrl] = None
    SECRET_KEY: Optional[str] = None
    ORIGINS: Optional[str] = None
    TEST_SQLALCHEMY_DATABASE_URI: Optional[AnyUrl] = None

    model_config = {"env_file": ".env"}


settings: Any = Settings()
config: str = Config(".env")
