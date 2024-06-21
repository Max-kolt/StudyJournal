from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from .repository import CurrentClassScheduleRepository
from src.entities.Groups.model import Group
from src.entities.Groups.repository import GroupRepository
from src.entities.Teachers.model import Teacher
from src.entities.Teachers.repository import TeacherRepository


class TimetableService:
    @staticmethod
    async def get_teacher_timetable(db: AsyncSession, teacher_id: str):
        teacher: Teacher = await TeacherRepository.get_by_user_id(db, teacher_id)

        if teacher:
            timetable = {
                "Понедельник":[],
                "Вторник":[],
                "Среда":[],
                "Четверг":[],
                "Пятница":[],
                "Суббота":[],
                "Воскресенье":[]
            }
            day = []
            for subject in teacher.subjects:
                current_lesson = {}

                for class_time in subject.class_timetable:
                    timetable[class_time.week_day].append(
                        {'lesson_number': class_time.lesson_number, 'name': subject.discipline_id, 'group': class_time.group_id,
                         'cabinet': class_time.cabinet})

            return timetable
        raise HTTPException(status_code=400, detail='Cant find teacher')

    @staticmethod
    async def get_lesson_dates(db: AsyncSession, group_id: str, lesson: int):
        lessons = await CurrentClassScheduleRepository.get_by_default_class(db, lesson)

        if lessons:
            # return lessons
            dates=[]
            month = {'month': 1, 'year': 2024, 'days': []}
            for lesson in lessons:
                if lesson.default_class.group_id == group_id:
                    if month['month'] == lesson.date_of.month:
                        month['days'].append(lesson.date_of.day)
                    else:
                        dates.append(month)
                        month = {'month': lesson.date_of.month, 'year': lesson.date_of.year, 'days': []}
                        month['year'] = lesson.date_of.year
                        month['days'].append(lesson.date_of.day)
            return dates

        raise HTTPException(status_code=400, detail='Cant find lesson')