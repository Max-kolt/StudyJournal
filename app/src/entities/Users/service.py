from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
import uuid

from src.utils import password_generator
from .model import User, UserAccount
from .schema import UserSchema, UserAccountSchema, ChangePasswordSchema
from .repository import UserRepository, UserAccountRepository
from ..Auth.schema import bcrypt_context


class UserService:
    @staticmethod
    async def create_user(db: AsyncSession, data: UserSchema)->User:
        verify = await UserRepository.get_by_mail(db, data.mail)
        if verify:
            raise HTTPException(status_code=400, detail='Mail already used')
        new_user = await UserRepository.create(db, id=uuid.uuid4(), **data.model_dump())
        return new_user

    @staticmethod
    async def create_user_account(db: AsyncSession, data: UserAccountSchema):
        verify = await UserAccountRepository.get_by_id(db, data.id)
        if verify:
            raise HTTPException(status_code=400, detail='Account already created')


        _password = password_generator() if not data.password else data.password

        model = data.model_dump()
        model['password'] = bcrypt_context.hash(_password)
        await UserAccountRepository.create(db, **model)
        model['password'] = _password
        return UserAccountSchema(**model)


    @staticmethod
    async def change_password(db, data: ChangePasswordSchema) -> bool:
        verify: UserAccount | None = await UserAccountRepository.get_by_id(db, data.id)
        if verify:
            if bcrypt_context.verify(data.old_password, verify.password):
                await UserAccountRepository.update(db, data.id, password=bcrypt_context.hash(data.new_password))
                return True
            raise HTTPException(status_code=400, detail='Invalid password')
        raise HTTPException(status_code=400, detail='Unreal user')
