from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from .repository import UserAccountRepository, UserRepository
from .service import UserService
from .schema import UserAccountSchema, UserSchema


users_router = APIRouter(prefix='/users', tags=['Users'])


@users_router.get('/get_user')
async def get_user(user_id: str, db: AsyncSession = Depends(get_async_session)):
    await UserRepository.get_by_id(db, user_id)


@users_router.post('/create_user')
async def create_user(request_data: UserSchema, db: AsyncSession = Depends(get_async_session)):
    await UserRepository.create(db, **request_data.model_dump())

@users_router.post('/create_user_account')
async def create_user(request_data: UserAccountSchema, db: AsyncSession = Depends(get_async_session)):
    await UserAccountRepository.create(db, **request_data.model_dump())

