from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    name: str
    token: Optional[str]


class UserCreate(UserBase):
    password: str
