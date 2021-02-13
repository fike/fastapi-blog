from typing import Any, Dict, Optional, Union

from pydantic import PostgresDsn, validator
from pydantic.env_settings import BaseSettings


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None


settings = Settings()
