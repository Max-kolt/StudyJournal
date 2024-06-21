from src.entities.Specializations.model import Specialization
from database import Base
from sqlalchemy import Column, Uuid, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.entities.Users.model import User


class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column('id', Integer, primary_key=True)
    user_id = Column('user_id', Uuid, ForeignKey(User.id), nullable=False, unique=True)
    specialization_id = Column('specialization', Integer, ForeignKey(Specialization.id))
    description = Column('description', String)
    education = Column('education', String)
    category = Column('category', String)

    user = relationship('User', lazy="selectin")
    sites = relationship('TeacherSite', back_populates='teacher', lazy='selectin')
    subjects = relationship('Subject', back_populates='teacher', lazy='selectin')


class TeacherSite(Base):
    __tablename__ = 'teacher_sites'

    id = Column('id', Integer, primary_key=True)
    teacher_id = Column('teacher_id', Integer, ForeignKey(Teacher.id), nullable=False)
    site = Column('site', String, nullable=False)

    teacher = relationship(Teacher, back_populates='sites', lazy='selectin')