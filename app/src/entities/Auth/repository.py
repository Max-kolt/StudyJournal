
from config import SECRET_AUTH_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from jose import jwt
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
