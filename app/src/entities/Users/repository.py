from src.abstract import BaseRepo
from .model import User, UserAccount
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class UserRepository(BaseRepo):
    model = User

    @classmethod
    async def get_by_mail(cls, db: AsyncSession, model_mail: str) -> model:
        query = select(cls.model).where(cls.model.mail == model_mail)
        return (await db.execute(query)).scalar_one_or_none()


class UserAccountRepository(BaseRepo):
    model = UserAccount
    