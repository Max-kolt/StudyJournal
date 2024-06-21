from sqlalchemy.orm import relationship

from database import Base
from sqlalchemy import Column, Integer, Uuid, ForeignKey, Null, Date, String, Boolean

from src.entities.Groups.model import Group
from src.entities.Timetable.model import CompletedLesson
from src.entities.Users.model import User


class Student(Base):
    __tablename__ = "students"

    id = Column('id', Integer, primary_key=True)
    user_id = Column('user_id', Uuid, ForeignKey(User.id), nullable=True)
    group_id = Column('group_id', String, ForeignKey(Group.id))
    course = Column('course', Integer, server_default='1')

    user = relationship('User', lazy='selectin')
    absence = relationship('StudentAbsence', lazy='selectin')
    evaluation = relationship('StudentEvaluation', lazy='selectin')
    homeworks = relationship('StudentHomeworks', lazy='selectin')
    group = relationship('Group', back_populates='students', lazy='selectin')


class StudentAbsence(Base):
    __tablename__ = "student_absences"

    id = Column('id', Integer, primary_key=True)
    student_id = Column('student_id', Integer, ForeignKey(Student.id), nullable=False)
    lesson_id = Column('lesson_id', Integer, ForeignKey(CompletedLesson.lesson_id), nullable=False)

    lesson = relationship('CompletedLesson', lazy='selectin')


class StudentEvaluation(Base):
    __tablename__ = "student_evaluation"

    id = Column('id', Integer, primary_key=True)
    student_id = Column('student_id', Integer, ForeignKey(Student.id), nullable=False)
    lesson_id = Column('lesson_id', Integer, ForeignKey(CompletedLesson.lesson_id), nullable=False)
    mark = Column('mark', Integer, nullable=False)

    lesson = relationship('CompletedLesson', lazy='selectin')


class StudentHomeworks(Base):
    __tablename__ = "student_homeworks"

    id = Column('id', Integer, primary_key=True)
    student_id = Column('student_id', Integer, ForeignKey(Student.id), nullable=False)
    lesson = Column('lesson_id', Integer, ForeignKey(CompletedLesson.lesson_id), nullable=False)
    homework_text = Column('homework_text', String)


