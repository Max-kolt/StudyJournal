from pydantic import BaseModel
from src.entities.Specializations.schema import SpecializationSchema


class GroupSchema(BaseModel):
    id: str
    specialization: int
    course: int


class LessonMarksSchema(BaseModel):
    group: str
    subject: str
