from sqlalchemy import Column, Uuid, DateTime, func, Boolean, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column('id', Uuid, primary_key=True)
    created_at = Column('created_at', DateTime, server_default=func.now())
    updated_at = Column("updated_at", DateTime, server_onupdate=func.now())

    fname = Column('fname', String)
    lname = Column('lname', String)
    mname = Column("mnema", String)
    mail = Column("mail", String, unique=True)
    phone = Column('phone', String)
    gender = Column('gender', String)
    with_account = Column('with_account', Boolean, server_default='f')

    account = relationship('UserAccount', back_populates='user', lazy='selectin')
    
    
class UserAccount(Base):
    __tablename__ = 'users_accounts'

    id = Column('id', Uuid,  ForeignKey(User.id), primary_key=True)
    created_at = Column('created_at', DateTime, server_default=func.now())
    updated_at = Column("updated_at", DateTime, server_onupdate=func.now())
    is_active = Column("is_active", Boolean, server_default="t")
    avatar = Column('avatar', String)
    password = Column('password', String, nullable=False)

    user = relationship(User, back_populates='account', lazy='selectin')
