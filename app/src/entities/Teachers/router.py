from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .repository import TeacherRepository
from .schema import teacher_dep, TeacherSchema

from src.entities.Auth.schema import admin_dep

from database import get_async_session
from .service import TeacherService

teacher_router = APIRouter(prefix='/teachers', tags=['Teachers'])


@teacher_router.get('/get_by_id/{user_id}')
async def get_me(user_id: str, current_user: teacher_dep, db: AsyncSession = Depends(get_async_session)):
    teacher = await TeacherRepository.get_by_user_id(db, user_id)
    return teacher


@teacher_router.get('/get_all')
async def get_all_teachers(current_user: admin_dep, db: AsyncSession = Depends(get_async_session)):
    all_teachers = await TeacherRepository.get_all(db)
    return all_teachers


@teacher_router.post('/create')
async def create_teacher(request_data: TeacherSchema, current_user: admin_dep, db: AsyncSession = Depends(get_async_session)):
    new_teacher = await TeacherService.create_teacher_user(db, request_data)
    return new_teacher

