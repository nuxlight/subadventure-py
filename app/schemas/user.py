from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    token: str


class UserCreate(UserBase):
    password: str
