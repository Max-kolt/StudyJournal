from src.entities.Specializations.model import Specialization
from database import Base
from sqlalchemy import Column, Uuid, Integer, String, ForeignKey
from src.entities.Users.model import User


class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column('id', Integer, primary_key=True)
    user_id = Column('user_id', Uuid, ForeignKey(User.id), nullable=True)
    specialization = Column('specialization', Integer, ForeignKey(Specialization.id))
    teaching_exp = Column('teaching_experience', Integer)

