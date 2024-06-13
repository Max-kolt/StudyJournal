from database import Base
from src.entities.Users.model import User
from src.entities.Students.model import Student
from sqlalchemy import Column, ForeignKey, Uuid, Integer


class StudentParents(Base):
    __tablename__ = 'student_parents'

    student_id = Column('student_id', Integer, ForeignKey(Student.id))
    parent_id = Column('parent_id', Uuid, ForeignKey(User.id), primary_key=True)
