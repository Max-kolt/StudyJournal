from pydantic import BaseModel


class SpecializationSchema(BaseModel):
    name: str
    qualification: str | None


class EducationalCycleSpecialization(BaseModel):
    specailization: int | SpecializationSchema
    ed_cycle: int

