from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .schema import AdminSchema, admin_dep
from database import get_async_session
from .service import AdminService

admin_router = APIRouter(prefix='/admin', tags=['Admin'])


@admin_router.post('/create_admin')
async def create_admin(current_user: admin_dep, request_body: AdminSchema, db: AsyncSession = Depends(get_async_session)):
    user = await AdminService.create_admin(db, request_body)
    return user
