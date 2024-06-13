
from datetime import datetime
from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError

from src.entities.Auth.repository import AuthRepository
from src.abstract.base_repo import BaseRepo
from .model import StudentParents


class ParentRepository(BaseRepo):
    model = StudentParents


admin_oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/parent_login')


async def verify_admin(token: Annotated[str, Depends(admin_oauth2_bearer)]):
    try:
        payload = await AuthRepository.decode_token(token)
        expire: int = payload.get('exp')
        if expire <= int(datetime.now().timestamp()):
            raise HTTPException(status_code=401, detail='token expired')

        mail: str = payload.get('mail')
        user_type: str = payload.get('user_type')

        if mail is None or user_type != 'parent':
            raise HTTPException(status_code=401, detail='Could not validate user.')

        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail='Could not validate user.')

