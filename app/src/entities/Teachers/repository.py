from datetime import datetime
from sqlalchemy import select
from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.ext.asyncio import AsyncSession

from src.entities.Auth.repository import AuthRepository
from src.abstract.base_repo import BaseRepo
from src.entities.Users.model import User
from .model import Teacher


class TeacherRepository(BaseRepo):
    model = Teacher

    @classmethod
    async def get_by_user_id(cls, db: AsyncSession, model_id: str) -> model:
        query = select(cls.model).where(cls.model.user_id == model_id)
        return (await db.execute(query)).scalar_one_or_none()


teacher_oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/teacher_login')


async def verify_teacher(token: Annotated[str, Depends(teacher_oauth2_bearer)]):
    try:
        payload = await AuthRepository.decode_token(token)
        expire: int = payload.get('exp')
        if expire <= int(datetime.now().timestamp()):
            raise HTTPException(status_code=401, detail='token expired')
        user_type: str = payload.get('user_type')
        if user_type == 'admin':
            return payload

        mail: str = payload.get('mail')
        if mail and user_type == 'teacher':
            return payload

        raise HTTPException(status_code=401, detail='Could not validate user.')


    except JWTError:
        raise HTTPException(status_code=401, detail='Could not validate user.')

