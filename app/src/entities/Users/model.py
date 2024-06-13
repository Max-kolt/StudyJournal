from sqlalchemy import Column, Uuid, DateTime, func, Boolean, String, ForeignKey

from database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column('id', Uuid, primary_key=True)
    created_at = Column('created_at', DateTime, server_default=func.now())
    updated_at = Column("updated_at", DateTime, server_onupdate=func.now())

    fname = Column('fname', String)
    lname = Column('lname', String)
    mname = Column("manema", String)
    email = Column("email", String, unique=True)
    phone = Column('phone', String)
    gander = Column('gander', String)
    
    
class UserAccount(Base):
    __tablename__ = 'users_accounts'

    id = Column('id', Uuid,  ForeignKey(User.id), primary_key=True)
    created_at = Column('created_at', DateTime, server_default=func.now())
    updated_at = Column("updated_at", DateTime, server_onupdate=func.now())
    is_active = Column("is_active", Boolean, server_default="t")
    avatar = Column('avatar', String)
    password = Column('password', String, nullable=False)
