from sqlalchemy.ext.asyncio import AsyncSession
from .schema import UserSchema
from .repository import UserRepository


class UserService:
    @staticmethod
    async def create_new_user(db: AsyncSession, data: UserSchema):
        pass

    @staticmethod
    async def create_user_account(db: AsyncSession, data: UserSchema):
        pass
