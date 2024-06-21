from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException

from .repository import GroupRepository
from src.entities.Teachers.repository import TeacherRepository
from .model import Group
from .schema import LessonMarksSchema
from datetime import datetime
from statistics import fmean

from ..Timetable.repository import SubjectRepository


class GroupService:
    @staticmethod
    async def get_teachers_groups(db: AsyncSession, teacher_id: str):
        teacher = await TeacherRepository.get_by_user_id(db, teacher_id)
        if teacher:
            # return teacher
            groups = list()
            fetched_subjects = list()
            for subject in teacher.subjects:
                fetched_subjects.append({
                    'subject': subject.discipline_id,
                    'groups': set(one_class.group_id for one_class in subject.class_timetable)
                })
                fetched_groups = [
                    {
                        'id': one_class.group_id,
                        "course": one_class.group.course,
                        'specialization': one_class.group.specialization.name,
                        'qualification': one_class.group.specialization.qualification,
                        'subjects': set(sub['subject'] for sub in fetched_subjects),
                        'students': [f"{student.user.lname} {student.user.fname}" for student in
                                     one_class.group.students]
                    }
                    for one_class in subject.class_timetable
                ]
                groups = [*groups, *fetched_groups]
            groups = list({v['id']: v for v in groups}.values())
            return groups
        raise HTTPException(detail='Cant find teacher', status_code=400)

    # @staticmethod
    # async def get_group_lesson_table(db: AsyncSession, group_id: str):
    #     await GroupService.get_group_lesson_table(db, '404')

    @staticmethod
    async def get_group_marks(db: AsyncSession, group: str, lesson: str):
        group: Group | None = await GroupRepository.get_by_id(db, group)
        if group:
            students_marks = {}
            subject_id=await SubjectRepository.get_by_disciplines(db, lesson)
            for student in group.students:
                marks_info = []
                current_date = None
                for marks in student.evaluation:

                    if marks.lesson.schedule_lesson.default_class.subject.discipline_id == lesson:
                        if current_date == marks.lesson.schedule_lesson.date_of:
                            marks_info[-1]["mark"].append({marks.id: marks.mark})

                        else:
                            marks_info.append({"mark": [{marks.id: marks.mark}],
                                               marks.lesson.schedule_lesson.date_of.month: marks.lesson.schedule_lesson.date_of.day})
                        current_date = marks.lesson.schedule_lesson.date_of

                sub_results = [fmean([val for m in mark['mark'] for val in m.values()]) for mark in marks_info]
                result_avg = sum(sub_results) / len(sub_results) if len(sub_results) != 0 else 0
                student_info = {
                    'id': student.id,
                    'name': f"{student.user.lname} {student.user.fname}",
                    'marks': marks_info,
                    'result': result_avg
                }
                students_marks[student.id] = student_info
            print(subject_id)
            return [students_marks, subject_id[0].id]
        raise HTTPException(detail='Cant find group', status_code=400)

    @staticmethod
    async def get_group_absences(db: AsyncSession, group_id: str):
        group = await GroupRepository.get_by_id(db, group_id)
        if group:
            return group
        raise HTTPException(detail='Cant find group', status_code=400)
