from typing import Optional

from pydantic import BaseModel, validator


class HTTPError(BaseModel):
    detail: str


class PostBase(BaseModel):
    title: str
    body: str


class PostCreate(PostBase):
    @validator("title")
    def validate_title(cls, title: str, **kwargs):
        if len(title) == 0:
            raise ValueError("Title can't be empty")
        elif len(title) > 100:
            raise ValueError("Title is too long")
        return title

    @validator("body")
    def validate_body(cls, body: str, **kwargs):
        if len(body) == 0:
            raise ValueError("Body can't be empty")
        return body


class Post(PostBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class Posts(Post):
    pass
