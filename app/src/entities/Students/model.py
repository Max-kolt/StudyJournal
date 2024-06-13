from database import Base
from sqlalchemy import Column, Integer, Uuid, ForeignKey, Null, Date, String, Boolean
from src.entities.Users.model import User


class Student(Base):
    __tablename__ = "students"

    id = Column('id', Integer, primary_key=True)
    user_id = Column('user_id', Uuid, ForeignKey(User.id), nullable=True)
    group = Column('group', String)
    course = Column('course', Integer)
    date_of_birth = Column('date_of_birth', Date)
    passport_series = Column('passport_series', String(4))
    passport_number = Column('passport_number', String(6))
    passport_issued_by = Column('passport_issued_by', String)
    passport_issued_date = Column('passport_issued_date', Date)
    is_verified = Column('is_verified', Boolean, server_default='True')

#
# class StudentAbsence(Base):
#     __tablename__ = "student_absences"
#
#     id = Column('id', Integer, primary_key=True)
#     student_id = Column('student_id', Integer, ForeignKey(Student.id), nullable=False)
#     lesson = Column('lesson_id', Integer, ForeignKey(CompletedLesson.id), nullable=False)
#
#
# class StudentEvulation(Base):
#     __tablename__ = "student_absences"
#
#     id = Column('id', Integer, primary_key=True)
#     student_id = Column('student_id', Integer, ForeignKey(Student.id), nullable=False)
#     lesson = Column('lesson_id', Integer, ForeignKey(CompletedLesson.id), nullable=False)
#
#
# class StudentHomeworks(Base):
#     __tablename__ = "student_absences"
#
#     id = Column('id', Integer, primary_key=True)
#     student_id = Column('student_id', Integer, ForeignKey(Student.id), nullable=False)
#     lesson = Column('lesson_id', Integer, ForeignKey(CompletedLesson.id), nullable=False)
#
