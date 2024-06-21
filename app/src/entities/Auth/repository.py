from typing import Annotated

from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer

from config import SECRET_AUTH_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from jose import jwt, JWTError
from datetime import datetime, timedelta


class AuthRepository:
    @staticmethod
    def create_token(data: dict) -> str:
        to_encode = data.copy()
        to_encode['exp'] = datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        return jwt.encode(to_encode, SECRET_AUTH_KEY, algorithm=ALGORITHM)

    @staticmethod
    async def decode_token(token: str):
        try:
            payload = jwt.decode(token, SECRET_AUTH_KEY, algorithms=[ALGORITHM])
            return payload
        except Exception:
            return {}


some_oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/manager_login')


async def verify_auth(token: Annotated[str, Depends(some_oauth2_bearer)]):
    try:
        payload = await AuthRepository.decode_token(token)
        expire: int = payload.get('exp')
        if expire <= int(datetime.now().timestamp()):
            raise HTTPException(status_code=401, detail='token expired')
        user_type: str = payload.get('user_type')

        if user_type not in ['admin', 'teacher', 'student']:
            raise HTTPException(status_code=401, detail='Could not validate user.')

        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail='Could not validate user.')
