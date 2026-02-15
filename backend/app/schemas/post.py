from datetime import datetime
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, StrictBool, field_validator


class PostBase(BaseModel):
    title: str
    body: str
    summary: str


class PostCreate(PostBase):
    @field_validator("title")
    def validate_title(cls: Any, title: str) -> Any:
        if len(title) == 0:
            raise ValueError("Title can't be empty")
        elif len(title) > 100:
            raise ValueError("Title is too long")
        return title

    @field_validator("summary")
    def validate_summary(cls: Any, summary: str) -> Any:
        if len(summary) == 0:
            raise ValueError("Summary can't be empty")
        elif len(summary) > 200:
            raise ValueError("Summary is too long")
        return summary

    @field_validator("body")
    def validate_body(cls: Any, body: str):
        if len(body) == 0:
            raise ValueError("Body can't be empty")
        return body


class PostInDB(PostBase):
    title: str
    body: str
    summary: str
    id: Optional[int] = None
    published_at: Optional[datetime] = None
    slug: Optional[str] = None
    author_id: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)


class Posts(PostInDB):
    pass


class PostUpdate(PostBase):
    # id: int
    author_id: int
