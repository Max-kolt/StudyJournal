from pydantic import BaseModel


class SpecializationSchema(BaseModel):
    name: str
    qualification: str | None


class EducationalCycleSpecializationSchema(BaseModel):
    specialization_id: int
    ed_cycle: int

