from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.entities.Auth.schema import admin_dep, auth_dep
from .service import UserService
from.schema import UserAccountSchema, ChangePasswordSchema
from database import get_async_session

user_router = APIRouter(prefix='/user', tags=['User'])


@user_router.post('/create_account')
async def create_account(request_data: UserAccountSchema, current_user: admin_dep, db: AsyncSession = Depends(get_async_session)):
    new_account = await UserService.create_user_account(db, request_data)
    return new_account


@user_router.post('/change_password')
async def create_account(request_data: ChangePasswordSchema, current_user: auth_dep, db: AsyncSession = Depends(get_async_session)):
    is_changed = await UserService.change_password(db, request_data)
    return {'ok': is_changed}
