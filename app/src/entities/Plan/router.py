from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from .repository import EducatoinCycleRepository, DisciplineRepository, CycleDesciplineRepository
from database import get_async_session
from src.entities.Auth.schema import admin_dep
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
    try:
        cycle = await DisciplineRepository.create(db, **request_body.model_dump())
    except IntegrityError as error:
        raise HTTPException(status_code=400, detail='Discipline already created')
    return cycle


@plan_router.delete('/delete_discipline')
async def delete_discipline(descipline_name: str, current_user: admin_dep, db: AsyncSession = Depends(get_async_session)):
    await DisciplineRepository.delete_by_name(db, descipline_name)
    return {'ok': True}


@plan_router.post('/add_discipline_to_cycle')
async def add_discipline_to_cycle(request_body: CycleDesciplineSchema, current_user: admin_dep, db: AsyncSession = Depends(get_async_session)):
    new_connection = await CycleDesciplineRepository.create(db, **request_body.model_dump())
    return new_connection


@plan_router.delete('/remove_discipline_from_cycle')
async def remove_discipline_from_cycle(cycle_discipline_id: int, current_user: admin_dep, db: AsyncSession = Depends(get_async_session)):
    await CycleDesciplineRepository.delete(db, cycle_discipline_id)
    return {'ok': True}