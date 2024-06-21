from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.entities.Plan.repository import EducationalCycle
from database import Base


class Specialization(Base):
    __tablename__ = "specializations"

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String, nullable=False)
    qualification = Column('qualification', String)

    cycles = relationship('EducationalCycleSpecialization', back_populates='specializations', lazy='selectin')
    groups = relationship('Group', back_populates='specialization', lazy='selectin')


class EducationalCycleSpecialization(Base):
    __tablename__ = "educational_cycle_specializations"

    id = Column('id', Integer, primary_key=True)
    specialization_id = Column('specialization', Integer, ForeignKey(Specialization.id))
    ed_cycle = Column('ed_cycle', Integer, ForeignKey(EducationalCycle.id))

    specializations = relationship(Specialization, back_populates='cycles', lazy='selectin')
    cycle = relationship('EducationalCycle', lazy='selectin')
