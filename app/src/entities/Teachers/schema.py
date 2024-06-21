from typing import Annotated
from fastapi import Depends
from pydantic import BaseModel

from src.entities.Users.schema import UserSchema

from src.entities.Teachers.repository import verify_teacher


class TeacherSchema(UserSchema):
    specialization_id: int | None
    education: str | None
    category: str | None


teacher_dep = Annotated[dict, Depends(verify_teacher)]
