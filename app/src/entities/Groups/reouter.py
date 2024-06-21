from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from statistics import mean
from database import get_async_session
from .repository import GroupRepository
from src.entities.Auth.schema import admin_dep
from src.entities.Teachers.schema import teacher_dep
from .schema import GroupSchema, LessonMarksSchema
from src.entities.Specializations.repository import SpecializationsRepository
from .service import GroupService

group_router = APIRouter(prefix='/groups', tags=['Groups'])


@group_router.get('/all')
async def get_all_groups(current_user: admin_dep, db: AsyncSession = Depends(get_async_session)):
    groups = await GroupRepository.get_all(db)
    return groups


@group_router.post('/create')
async def get_all_groups(request_data: GroupSchema, current_user: admin_dep,
                         db: AsyncSession = Depends(get_async_session)):
    specialization = await SpecializationsRepository.get_by_name_and_qualification(
        db, request_data.specialization.name, request_data.specialization.qualification
    )
    groups = await GroupRepository.create(db, id=request_data.id, course=request_data.course,
                                          specialization=specialization.id)
    return groups


@group_router.post('/get_by_id/{group_id}')
async def get_by_id(group_id: str, teacher: str, current_user: teacher_dep,
                    db: AsyncSession = Depends(get_async_session)):
    group = await GroupRepository.get_by_id(db, group_id)
    lessons = set([week_lesson.subject.discipline_id for week_lesson in group.classes_timetable if
                   str(week_lesson.subject.teacher.user_id) == teacher])
    group_students = [{'fullname': f"{student.user.lname} {student.user.fname}", "id": student.id} for student in
                      group.students]
    return {"id": group.id, 'course': group.course, 'students': group_students, "lessons": lessons}


@group_router.post('/get_avarage/{group_id}')
async def get_by_id(group_id: str, lesson: str, current_user: teacher_dep,
                    db: AsyncSession = Depends(get_async_session)):
    group = await GroupRepository.get_by_id(db, group_id)
    group_students = [
        {'fullname': f"{student.user.lname} {student.user.fname}", "id": student.id,
         'result': [marks.mark for marks in student.evaluation if
                    marks.lesson.schedule_lesson.default_class.subject.discipline_id == lesson]}
        for student in group.students
    ]
    group_students = [{**stud, "result": int(sum(stud['result']) / len(stud['result'])) if len(stud['result']) != 0 else 0}
                      for stud in group_students]

    return {"id": group.id, 'course': group.course, 'students': group_students}


@group_router.get('/get_teacher_groups')
async def get_teacher_groups(teacher_id: str, current_user: teacher_dep, db: AsyncSession = Depends(get_async_session)):
    groups = await GroupService.get_teachers_groups(db, teacher_id)
    return groups


@group_router.get('/get_group_marks')
async def get_group_marks(group: str, lesson: str, current_user: teacher_dep,
                          db: AsyncSession = Depends(get_async_session)):
    group_marks, subject = await GroupService.get_group_marks(db, group, lesson)
    return {'group_marks': group_marks, 'subject': subject}


@group_router.get('/get_group_absences')
async def get_group_absences(group_id: str, current_user: teacher_dep, db: AsyncSession = Depends(get_async_session)):
    group_marks = await GroupService.get_group_absences(db, group_id)
    return group_marks
# @group_router.get('/get_students_table')
# async def get_students_table():
#     pass
#
#
# @group_router.get('/get_students_xlsx')
# async def get_students_xlsx():
#     pass
