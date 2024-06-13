from pydantic import BaseModel
from typing import Literal


class UserSchema(BaseModel):
    fname: str
    lname: str
    mname: str
    email: str
    phone: str | None
    gender: Literal['male', 'female']

class UserAccountSchema(BaseModel):
    email: str
    password: str | None
    