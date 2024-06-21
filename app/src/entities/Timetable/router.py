from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from src.entities.Auth.schema import teacher_dep
from .repository import ClassesTimetableRepository, SubjectRepository
from .service import TimetableService

timetable_router = APIRouter(prefix='/timetable', tags=['Timetable'])


@timetable_router.get('/get_teacher_timetable')
async def get_teacher_timetable(teacher_id: str, current_user: teacher_dep, db: AsyncSession = Depends(get_async_session)):
    techaer_timetable = await TimetableService.get_teacher_timetable(db, teacher_id)
    return techaer_timetable


@timetable_router.get('/get_lesson_dates')
async def get_lesson_dates(group: str, lesson: int, current_user: teacher_dep, db: AsyncSession = Depends(get_async_session)):
    lesson_dates = await TimetableService.get_lesson_dates(db, group, lesson)
    return lesson_dates


@timetable_router.get('/subject')
async def get_some(lesson: str, current_user: teacher_dep, db: AsyncSession = Depends(get_async_session)):
    classes = await SubjectRepository.get_by_id(db, lesson)
    return classes.subject.discipline_id

