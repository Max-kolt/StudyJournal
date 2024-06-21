from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .repository import AdminRepository
from .schema import AdminSchema
from database import get_async_session
from .service import AdminService
from src.entities.Auth.schema import admin_dep

admin_router = APIRouter(prefix='/admin', tags=['Admin'])


@admin_router.post('/create')
async def create_admin(current_user: admin_dep, request_body: AdminSchema, db: AsyncSession = Depends(get_async_session)):
    user = await AdminService.create_admin(db, request_body)
    return user


@admin_router.get('/all')
async def create_admin(current_user: admin_dep, db: AsyncSession = Depends(get_async_session)):
    all_user = await AdminRepository.get_all(db)
    return all_user