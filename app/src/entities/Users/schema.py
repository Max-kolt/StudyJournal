from pydantic import BaseModel
from typing import Literal


class UserSchema(BaseModel):
    fname: str
    lname: str
    mname: str
    mail: str
    phone: str | None
    gender: Literal['male', 'female']


class UserAccountSchema(BaseModel):
    id: str
    password: str | None


class ChangePasswordSchema(BaseModel):
    id: str
    old_password: str
    new_password: str
