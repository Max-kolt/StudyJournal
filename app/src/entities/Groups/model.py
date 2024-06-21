from sqlalchemy import ForeignKey, String, Integer, Column, ForeignKey
from sqlalchemy.orm import relationship

from database import Base
from src.entities.Specializations.model import Specialization


class Group(Base):
    __tablename__ = 'groups'

    id = Column('id', String, primary_key=True)
    specialization_id = Column('specialization', Integer, ForeignKey(Specialization.id))
    course = Column('course', Integer)

    students = relationship('Student', back_populates='group', lazy='selectin')
    specialization = relationship('Specialization', back_populates='groups', lazy='selectin')
    classes_timetable = relationship('ClassesTimetable', back_populates='group', lazy='selectin')