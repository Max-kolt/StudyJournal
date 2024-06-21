from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from .repository import StudentRepository, StudentAbsenceRepository, StudentEvaluationRepository
from .schema import StudentSchema, StudentAddMarkSchema, StudentRemoveMarkSchema, StudentLessonSchema
from .model import StudentEvaluation
from src.entities.Auth.schema import bcrypt_context
from src.entities.Auth.repository import AuthRepository
from src.entities.Users.repository import UserRepository
from fastapi import HTTPException

from ..Groups.repository import GroupRepository
from ..Timetable.repository import CurrentClassScheduleRepository
from ..Users.service import UserService
from ..Users.schema import UserSchema
from statistics import mean


class StudentService:
    @staticmethod
    async def login(db: AsyncSession, login: OAuth2PasswordRequestForm):
        user = await UserRepository.get_by_mail(db, login.username)
        is_student = await StudentRepository.get_by_user_id(db, user.id)
        if is_student and user:
            if bcrypt_context.verify(login.password, user.account[0].password):
                return (
                    AuthRepository.create_token(data={'mail': login.username, 'user_type': 'student'}),
                    {'id': user.id, 'mail': user.mail}
                )
        raise HTTPException(status_code=400, detail='Name or password not valid')

    @staticmethod
    async def create_student_user(db: AsyncSession, data: StudentSchema):
        verify = await UserRepository.get_by_mail(db, data.mail)
        if verify:
            raise HTTPException(status_code=400, detail='Mail already taken')
        verify = await GroupRepository.get_by_id(db, data.group_id)
        if not verify:
            raise HTTPException(status_code=400, detail='Group not found')

        user_data = UserSchema(
            fname=data.fname,
            lname=data.lname,
            mname=data.mname,
            mail=data.mail,
            phone=data.phone,
            gender=data.gender
        )
        user_model = await UserService.create_user(db, user_data)
        student_model = await StudentRepository.create(
            db, user_id=user_model.id, group_id=data.group_id, course=data.course,
        )

        return {**student_model.__dict__, 'user': user_data.model_dump()}

    @staticmethod
    async def add_mark(db: AsyncSession, data: StudentAddMarkSchema):
        lessons = await CurrentClassScheduleRepository.get_by_default_class(db, data.lesson_id)
        for lesson in lessons:
            if lesson.date_of.month == data.month and lesson.date_of.day == data.day:
                if data.mark != 'Н':
                    reformat_mark = {'student_id':data.student_id, 'lesson_id':lesson.id, 'mark':int(data.mark)}
                    new_mark: StudentEvaluation = await StudentEvaluationRepository.create(db, **reformat_mark)
                    student_marks = await StudentEvaluationRepository.get_student_marks(db, data.student_id)
                    marks_list = [mark.mark for mark in student_marks]
                    return {'new_result': sum(marks_list)/ len(marks_list) if len(marks_list)!=0 else 0}
                else:
                    check = await StudentAbsenceRepository.get_student_lesson(db, data.student_id, data.lesson_id)
                    if not check:
                        await StudentAbsenceRepository.create(db, student_id=data.student_id, lesson_id=lesson.id)
                        return {'ok': True}
        raise HTTPException(status_code=400, detail='cant add mark')

    @staticmethod
    async def delete_mark(db: AsyncSession, data: StudentLessonSchema):
        lessons = await CurrentClassScheduleRepository.get_by_default_class(db, data.lesson_id)

        for lesson in lessons:
            if lesson.date_of.month == data.month and lesson.date_of.day == data.day:
                evaluations = await StudentEvaluationRepository.get_student_lesson(db, data.student_id, lesson.id)
                for eval in evaluations:
                    await StudentEvaluationRepository.delete(db, eval.id)
                student_marks = await StudentEvaluationRepository.get_student_lesson(db, data.student_id, data.lesson_id)
                marks_list = [mark.mark for mark in student_marks]
                abcense = await StudentAbsenceRepository.get_student_lesson(db, data.student_id, lesson.id)
                if not abcense:
                    return {'new_result': sum(marks_list) / len(marks_list) if len(marks_list) != 0 else 0}
                for abce in abcense:
                    await StudentAbsenceRepository.delete(db, abce.id)

                return {'new_result': sum(marks_list) / len(marks_list) if len(marks_list) != 0 else 0}




    # @staticmethod
    # async def toggle_student_absence(db: AsyncSession, data: StudentLessonSchema):
    #     check = await StudentAbsenceRepository.get_student_lesson(db, data.student_id, data.lesson_id)
    #     if check:
    #         await StudentAbsenceRepository.delete(db, check.id)
    #     else:
    #         await StudentAbsenceRepository.create(db, **data.model_dump())

