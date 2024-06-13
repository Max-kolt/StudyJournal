from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from src.entities.Auth.schema import bcrypt_context
from src.entities.Auth.repository import AuthRepository
from src.entities.Users.repository import UserRepository
from fastapi import HTTPException


class ParentService:
    @staticmethod
    async def login(db: AsyncSession, login: OAuth2PasswordRequestForm):
        user = await UserRepository.get_by_mail(db, login.username)
        if user:
            if bcrypt_context.verify(login.password, user.password):
                return AuthRepository.create_token(data={'mail': login.username, 'user_type': 'parent'})
        raise HTTPException(status_code=400, detail='Name or password not valid')
