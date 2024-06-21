from typing import Annotated
from datetime import date
from fastapi import Depends
from pydantic import BaseModel

from .repository import verify_student
from src.entities.Users.schema import UserSchema


class StudentSchema(UserSchema):
    group_id: str
    course: int | None


class StudentLessonSchema(BaseModel):
    student_id: int
    lesson_id: int
    day: int
    month: int


class StudentRemoveMarkSchema(StudentLessonSchema):
    id: list[int]


class StudentAddMarkSchema(StudentLessonSchema):
    mark: str

