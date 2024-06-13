from .model import Specialization, EducationalCycleSpecialization
from src.abstract import BaseRepo


class SpecializationsRepository(BaseRepo):
    model = Specialization


class EducationalCycleSpecializationRepository(BaseRepo):
    model = EducationalCycleSpecialization
