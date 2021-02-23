from typing import Optional

from pydantic import BaseModel, StrictBool, validator


class UserBase(BaseModel):
    username: str
    profile: str
    email: str
    disabled: StrictBool = False


class UserCreate(UserBase):
    password: str

    @validator("username")
    def validate_username(cls, username: str, **kwargs):
        if len(username) <= 4:
            raise ValueError("Username can't be empty")
        return username

    @validator("email")
    def validate_email(cls, email: str, **kwargs):
        if len(email) == 0:
            raise ValueError("An email is required")
        return email

    @validator("profile")
    def validate_profile(cls, profile: str, **kwargs):
        if len(profile) == 0:
            raise ValueError("A profile is required")
        return profile


class User(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class UserInDB(User):
    hashed_password: str


class Users(User):
    id: int
