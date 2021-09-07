from typing import Optional

from pydantic import BaseModel, StrictBool, validator


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
