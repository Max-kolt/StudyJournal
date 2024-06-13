from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .repository import SpecializationsRepository
from database import get_async_session
from src.entities.AdminPanel.schema import admin_dep
from .schema import SpecializationSchema

specializations_router = APIRouter(prefix='/specializations', tags=['Specialization'])


@specializations_router.get('/get_all')
async def get_all(current_user: admin_dep, db: AsyncSession = Depends(get_async_session)):
    specializations = await SpecializationsRepository.get_all(db)
    return specializations


@specializations_router.post('/create')
async def create(request_body: SpecializationSchema, current_user: admin_dep, db: AsyncSession = Depends(get_async_session)):
    specializations = await SpecializationsRepository.create(db, **request_body.model_dump())
    return specializations


@specializations_router.delete('/delete')
async def create(specialization_id: int, current_user: admin_dep, db: AsyncSession = Depends(get_async_session)):
    await SpecializationsRepository.delete(db, specialization_id)
    return {'ok': True}


