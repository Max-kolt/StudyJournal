from sqlalchemy import Column, Integer, String, ForeignKey

from src.entities.Plan.repository import EducationalCycle
from database import Base


class Specialization(Base):
    __tablename__ = "specializations"

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String, nullable=False)
    qualification = Column('qualification', String)


class EducationalCycleSpecialization(Base):
    __tablename__ = "educational_cycle_specializations"

    id = Column('id', Integer, primary_key=True)
    specialization = Column('specialization', Integer, ForeignKey(Specialization.id))
    ed_cycle = Column('ed_cycle', Integer, ForeignKey(EducationalCycle.id))
