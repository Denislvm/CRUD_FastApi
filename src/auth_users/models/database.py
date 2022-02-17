from pydantic import BaseModel, EmailStr
from datetime import date


class Model(BaseModel):
    id: int
    username: str
    email: EmailStr
    password: str
    date: date

    class Config:
        orm_mode = True


class UserID(Model):
    id: int

    class Config:
        orm_mode = True


class UserCreate(Model):
    pass


class UserUpdate(Model):
    pass
