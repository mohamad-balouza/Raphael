from pydantic import BaseModel, EmailStr
from typing import List, Optional


class UserBase(BaseModel):
    username: str
    email: EmailStr | None = None
    is_active: bool | None = True
    user_type_id: int = 2

class UserCreate(UserBase):
    email: EmailStr
    password: str

class UserUpdate(UserBase):
    password: str| None = None

class UserInDBBase(UserBase):
    id: int | None = None

    class Config:
        orm_mode = True

class User(UserInDBBase):
    user_type: Optional["UserTypeInDBBase"]

class UserInDB(UserInDBBase):
    hashed_password: str


from app.schemas.user_type import UserTypeInDBBase
User.update_forward_refs()