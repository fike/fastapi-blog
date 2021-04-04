from typing import Any, Optional

from pydantic import BaseModel, StrictBool, validator

from app.db.session import Base


class UserBase(BaseModel):
    username: str
    profile: str
    email: str
    disabled: StrictBool = False


class UserCreate(UserBase):
    password: str

    @validator("username")
    def validate_username(cls: Any, username: str, **kwargs: Any) -> Any:
        if len(username) <= 4:
            raise ValueError("Username can't be empty")
        return username

    @validator("email")
    def validate_email(cls: Any, email: str, **kwargs: Any) -> Any:
        if len(email) == 0:
            raise ValueError("An email is required")
        return email

    @validator("profile")
    def validate_profile(cls: any, profile: str, **kwargs: Any) -> Any:
        if len(profile) == 0:
            raise ValueError("A profile is required")
        return profile


class User(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode: bool = True


class UserInDB(User):
    hashed_password: str


class Users(User):
    id: int


class UserUpdate(UserBase):
    password: Optional[str]

    class Config:
        orm_mode: bool = True


class UserPassword(BaseModel):
    password: Optional[str] = None
    # pass
