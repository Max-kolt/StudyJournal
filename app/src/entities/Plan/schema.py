from pydantic import BaseModel


class EducationalCycleSchema(BaseModel):
    name: str
    curriculum_index: str | None


class DisciplineSchema(BaseModel):
    name: str
    curriculum_index: str | None
    course_of_study_max: int | None


class CycleDesciplineSchema(BaseModel):
    discipline_id: str
    education_cycle_id: int
    course_of_study: int
    academic_hours: int
