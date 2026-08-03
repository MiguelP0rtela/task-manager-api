from app.core.validators import validate_password

from pydantic import BaseModel, ConfigDict, EmailStr, field_validator


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

    @field_validator(validate_password(password))
    @classmethod
    def validate_user_password(cls, value: str):
        return validate_password(value)


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    email: str


class UserUpdate(BaseModel):
    username: str
    email: EmailStr


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserPasswordUpdate(BaseModel):
    old_password: str
    new_password: str

    @field_validator("new_password")
    @classmethod
    def validate_new_password(cls, value: str):
        return validate_password(value)
