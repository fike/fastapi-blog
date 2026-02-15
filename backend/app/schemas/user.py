from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, StrictBool, field_validator


class UserBase(BaseModel):
    username: str
    profile: str
    email: str
    disabled: StrictBool = False


class UserCreate(UserBase):
    password: str

    @field_validator("username")
    def validate_username(cls: Any, username: str) -> Any:
        if len(username) <= 4:
            raise ValueError("Username can't be empty")
        return username

    @field_validator("email")
    def validate_email(cls: Any, email: str) -> Any:
        if len(email) == 0:
            raise ValueError("An email is required")
        return email

    @field_validator("profile")
    def validate_profile(cls: Any, profile: str) -> Any:
        if len(profile) == 0:
            raise ValueError("A profile is required")
        return profile


class User(UserBase):
    id: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)


class UserInDB(User):
    hashed_password: str


class Users(User):
    id: int


class UserUpdate(UserBase):
    password: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class UserPassword(BaseModel):
    password: Optional[str] = None
    # pass
