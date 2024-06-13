from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from src.entities.Auth.repository import AuthRepository
from src.entities.Auth.schema import bcrypt_context
from src.utils import password_generator
from .schema import AdminSchema
from .repository import AdminRepository
from fastapi import HTTPException


class AdminService:
    @staticmethod
    async def create_admin(db: AsyncSession, request_body: AdminSchema):
        _verify = await AdminRepository.get_by_name(db, request_body.name)
        if _verify:
            raise HTTPException(status_code=400, detail='Username already taken.')

        _password = password_generator() if not request_body.password else request_body.password

        model = request_body.model_dump()
        model['password'] = bcrypt_context.hash(_password)
        await AdminRepository.create(db, **model)
        model['password'] = _password
        return AdminSchema(**model)

    @staticmethod
    async def login(db: AsyncSession, login: OAuth2PasswordRequestForm):
        user = await AdminRepository.get_by_name(db, login.username)
        if user:
            if bcrypt_context.verify(login.password, user.password):
                return AuthRepository.create_token(data={
                    'username': login.username,
                    'user_type': 'admin'
                })
        raise HTTPException(status_code=400, detail='Name or password not valid')


