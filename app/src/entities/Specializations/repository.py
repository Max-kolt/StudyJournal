from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession

from .model import Specialization, EducationalCycleSpecialization
from src.abstract import BaseRepo


class SpecializationsRepository(BaseRepo):
    model = Specialization

    @classmethod
    async def get_by_name_and_qualification(cls, db: AsyncSession, name: str, qualification: str) -> Specialization:
        query = select(cls.model).where(cls.model.name == name and cls.model.qualification == qualification)
        return (await db.execute(query)).scalar_one_or_none()


class EducationalCycleSpecializationRepository(BaseRepo):
    model = EducationalCycleSpecialization
