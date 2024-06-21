from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .repository import SpecializationsRepository, EducationalCycleSpecializationRepository
from database import get_async_session
from src.entities.Auth.schema import admin_dep
from .schema import SpecializationSchema, EducationalCycleSpecializationSchema

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
async def delete(specialization_id: int, current_user: admin_dep, db: AsyncSession = Depends(get_async_session)):
    await SpecializationsRepository.delete(db, specialization_id)
    return {'ok': True}


@specializations_router.post('/add_cycle')
async def create(request_body: EducationalCycleSpecializationSchema, current_user: admin_dep, db: AsyncSession = Depends(get_async_session)):
    specialization_cycle = await EducationalCycleSpecializationRepository.create(db, **request_body.model_dump())
    new_spec = await SpecializationsRepository.get_by_id(db, request_body.specialization_id)
    return new_spec


@specializations_router.delete('/remove_cycle')
async def delete(connect_id: int, current_user: admin_dep, db: AsyncSession = Depends(get_async_session)):
    await EducationalCycleSpecializationRepository.delete(db, connect_id)
    return {'ok': True}
