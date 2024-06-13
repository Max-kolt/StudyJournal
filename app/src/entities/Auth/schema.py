from passlib.context import CryptContext
from pydantic import BaseModel

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated="auto")

