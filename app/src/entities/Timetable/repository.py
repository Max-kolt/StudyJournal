from sqlalchemy import select

from src.abstract import BaseRepo
from .model import Subject, StandardClassSchedule, ReplacementClasses, ClassesTimetable, CurrentClassSchedule, CompletedLesson
from sqlalchemy.ext.asyncio import AsyncSession


class SubjectRepository(BaseRepo):
    model = Subject

    @classmethod
    async def get_by_disciplines(cls, db: AsyncSession, discipline_id: str):
        query = select(cls.model).where(cls.model.discipline_id == discipline_id)
        return (await db.execute(query)).scalars().all()

class StandardClassScheduleRepository(BaseRepo):
    model = StandardClassSchedule


class ReplacementClassesRepository(BaseRepo):
    model = ReplacementClasses


class ClassesTimetableRepository(BaseRepo):
    model = ClassesTimetable


class CurrentClassScheduleRepository(BaseRepo):
    model = CurrentClassSchedule

    @classmethod
    async def get_by_default_class(cls, db: AsyncSession, default_class_id: int):
        query = select(cls.model).where(cls.model.default_class_id == default_class_id)
        return (await db.execute(query)).scalars().all()

    @classmethod
    async def get_by_id(cls, db: AsyncSession, model_id: str | int):
        query = select(cls.model).where(cls.model.id == model_id)
        return (await db.execute(query)).scalars().all()


class CompletedLessonRepository(BaseRepo):
    model = CompletedLesson

