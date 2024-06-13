from database import Base
from sqlalchemy import Column, String


class HeadOfDepartment(Base):
    __tablename__ = 'head_of_department'

    name = Column('name', String, primary_key=True)
    password = Column('password', String)
