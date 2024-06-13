from sqlalchemy import Column, Integer, String, ForeignKey

from database import Base


class EducationalCycle(Base):
    __tablename__ = 'educational_cycle'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String, nullable=False)
    curriculum_index = Column('curiculum_index', String)


class Discipline(Base):
    __tablename__ = 'disciplines'

    name = Column('name', String, primary_key=True)
    curiculum_index = Column('curiculum_index', String)
    course_of_study_max = Column('course_of_study_max', Integer)


class CycleDescipline(Base):
    __tablename__ = 'cycle_desciplines'

    id = Column('id', Integer, primary_key=True)
    education_cycle = Column('educaation_cycle', Integer, ForeignKey(EducationalCycle.id))
    discipline = Column('discipline', String, ForeignKey(Discipline.name))
    course_of_study = Column('course_of_study', Integer)
    academic_hours = Column('academic_hours', Integer)
