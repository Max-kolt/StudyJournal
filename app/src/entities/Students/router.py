from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from .repository import StudentRepository
from .schema import StudentSchema, StudentAddMarkSchema, StudentRemoveMarkSchema, StudentLessonSchema
from src.entities.Auth.schema import admin_dep, student_dep
from .service import StudentService
from src.entities.Teachers.schema import teacher_dep

student_router = APIRouter(prefix='/students', tags=['Students'])


@student_router.get('/get_by_id/{user_id}')
async def get_student(user_id: str, current_user: student_dep, db: AsyncSession = Depends(get_async_session)):
    student = await StudentRepository.get_by_user_id(db, user_id)
    return student


@student_router.get('/all')
async def get_all_students(current_user: admin_dep, db: AsyncSession = Depends(get_async_session)):
    all_students = await StudentRepository.get_all(db)
    return all_students


@student_router.get('/from_group/{group_id}')
async def get_group_students(group_id: str, current_user: teacher_dep, db: AsyncSession = Depends(get_async_session)):
    student = await StudentRepository.get_from_group(db, group_id)
    return student


@student_router.post('/create')
async def create_student(request_data: StudentSchema, current_user: admin_dep, db: AsyncSession = Depends(get_async_session)):
    new_student = await StudentService.create_student_user(db, request_data)
    return new_student


@student_router.post('/insert_mark')
async def insert_mark(request_data: StudentAddMarkSchema, current_user: teacher_dep, db: AsyncSession = Depends(get_async_session)):
    print(request_data.model_dump())
    new_student_info = await StudentService.add_mark(db, request_data)
    return new_student_info


@student_router.post('/remove_marks')
async def remove_mark(request_data: StudentLessonSchema, current_user: teacher_dep, db: AsyncSession = Depends(get_async_session)):
    new_student_info = await StudentService.delete_mark(db, request_data)
    return new_student_info




@student_router.post('/toggle_absence')
async def toggle_absence(request_data: StudentLessonSchema, current_user: teacher_dep, db: AsyncSession = Depends(get_async_session)):
    await StudentService.toggle_student_absence(db, request_data)
    return {'ok': True}
