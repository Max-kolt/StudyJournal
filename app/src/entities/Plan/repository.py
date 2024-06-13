from src.abstract import BaseRepo
from .model import EducationalCycle, CycleDescipline, Discipline


class EducatoinCycleRepository(BaseRepo):
    model = EducationalCycle


class CycleDesciplineRepository(BaseRepo):
    model = CycleDescipline


class DisciplineRepository(BaseRepo):
    model = Discipline
