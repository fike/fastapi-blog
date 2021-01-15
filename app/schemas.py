from typing import List, Optional
from pydantic import BaseModel, validator

class HTTPError(BaseModel):
    detail: str

class PostBase(BaseModel):
    # title: Optional[str] = None
    title: str

class PostCreate(PostBase):
    # title: Optional[str] = None
    # pass

    @validator("title")
    def validate_title(cls, title: str, **kwargs):
        if len(title) == 0:
            raise ValueError("Title can't be null")
        elif len(title) > 200:
            raise ValueError("Title is too long")
        return title

class Post(PostBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True