from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .repository import EducatoinCycleRepository, DisciplineRepository, CycleDesciplineRepository
from database import get_async_session
from src.entities.AdminPanel.schema import admin_dep
from .schema import DisciplineSchema, EducationalCycleSchema, CycleDesciplineSchema

plan_router = APIRouter(prefix='/plan', tags=['Plan'])


@plan_router.get('/get_all_cycles')
async def get_all(current_user: admin_dep, db: AsyncSession = Depends(get_async_session)):
    cycles = await EducatoinCycleRepository.get_all(db)
    return cycles


@plan_router.post('/create_cycle')
async def create(request_body: EducationalCycleSchema, current_user: admin_dep, db: AsyncSession = Depends(get_async_session)):
    cycle = await EducatoinCycleRepository.create(db, **request_body.model_dump())
    return cycle


@plan_router.delete('/delete_cycle')
async def delete(cycle_id: int, current_user: admin_dep, db: AsyncSession = Depends(get_async_session)):
    await EducatoinCycleRepository.delete(db, cycle_id)
    return {'ok': True}


@plan_router.get('/get_all_disciplines')
async def get_all_disciplines(current_user: admin_dep, db: AsyncSession = Depends(get_async_session)):
    cycles = await DisciplineRepository.get_all(db)
    return cycles


@plan_router.post('/create_discipline')
async def create_discipline(request_body: DisciplineSchema, current_user: admin_dep, db: AsyncSession = Depends(get_async_session)):
    cycle = await DisciplineRepository.create(db, **request_body.model_dump())
    return cycle


@plan_router.delete('/delete_discipline')
async def delete_discipline(descipline_name: str, current_user: admin_dep, db: AsyncSession = Depends(get_async_session)):
    await DisciplineRepository.delete_by_name(db, descipline_name)
    return {'ok': True}


