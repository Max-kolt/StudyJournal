from datetime import datetime
from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError

from src.entities.Auth.repository import AuthRepository
from src.abstract.base_repo import BaseRepo
from .model import HeadOfDepartment
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


class AdminRepository(BaseRepo):
    model = HeadOfDepartment

    @classmethod
    async def get_by_name(cls, db: AsyncSession, model_name: str) -> HeadOfDepartment | None:
        query = select(cls.model).where(cls.model.name == model_name)
        return (await db.execute(query)).scalar_one_or_none()


admin_oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/manager_login')


async def verify_admin(token: Annotated[str, Depends(admin_oauth2_bearer)]):
    try:
        payload = await AuthRepository.decode_token(token)
        expire: int = payload.get('exp')
        if expire <= int(datetime.now().timestamp()):
            raise HTTPException(status_code=401, detail='token expired')

        username: str = payload.get('username')
        user_type: str = payload.get('user_type')

        if username is None or user_type != 'admin':
            raise HTTPException(status_code=401, detail='Could not validate user.')

        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail='Could not validate user.')

