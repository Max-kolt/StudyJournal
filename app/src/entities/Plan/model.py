from sqlalchemy import Uuid, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class EducationalCycle(Base):
    __tablename__ = 'educational_cycle'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String, nullable=False)
    curriculum_index = Column('curriculum_index', String)

    cycle_disciplines = relationship('CycleDescipline', back_populates='education_cycle', lazy='selectin')


class Discipline(Base):
    __tablename__ = 'disciplines'

    name = Column('name', String, primary_key=True)
    curriculum_index = Column('curriculum_index', String)
    course_of_study_max = Column('course_of_study_max', Integer)


class CycleDescipline(Base):
    __tablename__ = 'cycle_desciplines'

    id = Column('id', Integer, primary_key=True)
    education_cycle_id = Column('education_cycle', Integer, ForeignKey(EducationalCycle.id))
    discipline_id = Column('discipline', String, ForeignKey(Discipline.name))
    course_of_study = Column('course_of_study', Integer)
    academic_hours = Column('academic_hours', Integer)

    discipline = relationship(Discipline, lazy='selectin')
    education_cycle = relationship(EducationalCycle, back_populates='cycle_disciplines', lazy="selectin")
