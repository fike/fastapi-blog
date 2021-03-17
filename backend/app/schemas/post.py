from datetime import datetime
from typing import Any, Optional

from pydantic import BaseModel, StrictBool, validator


class PostBase(BaseModel):
    title: str
    body: str
    summary: str


class PostCreate(PostBase):
    @validator("title")
    def validate_title(cls: Any, title: str, **kwargs: Any) -> Any:
        if len(title) == 0:
            raise ValueError("Title can't be empty")
        elif len(title) > 100:
            raise ValueError("Title is too long")
        return title

    @validator("summary")
    def validate_summary(cls: Any, summary: str, **kwargs: Any) -> Any:
        if len(summary) == 0:
            raise ValueError("Title can't be empty")
        elif len(summary) > 200:
            raise ValueError("Title is too long")
        return summary

    @validator("body")
    def validate_body(cls: Any, body: str, **kwargs: Any):
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
    author_id: Optional[str] = None

    class Config:
        orm_mode: bool = True


class Posts(PostInDB):
    pass


class PostUpdate(PostBase):
    # id: int
    author_id: str
