from datetime import datetime
from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.entities.Auth.repository import AuthRepository
from src.abstract.base_repo import BaseRepo
from .model import Student, StudentAbsence, StudentEvaluation


class StudentAbsenceRepository(BaseRepo):
    model = StudentAbsence

    @classmethod
    async def get_student_lesson(cls, db: AsyncSession, stud_id: int, lesson_id: int) -> model:
        query = select(cls.model).where(cls.model.student_id == stud_id and cls.model.lesson_id == lesson_id)
        return (await db.execute(query)).scalar_one_or_none()


class StudentEvaluationRepository(BaseRepo):
    model = StudentEvaluation

    @classmethod
    async def get_student_lesson(cls, db: AsyncSession, stud_id: int, lesson_id: int) -> model:
        query = select(cls.model).where(cls.model.student_id == stud_id and cls.model.lesson_id == lesson_id)
        return (await db.execute(query)).scalars().all()


    @classmethod
    async def get_student_marks(cls, db: AsyncSession, stud_id: int) -> model:
        query = select(cls.model).where(cls.model.student_id == stud_id)
        return (await db.execute(query)).scalars().all()


class StudentRepository(BaseRepo):
    model = Student

    @classmethod
    async def get_by_user_id(cls, db: AsyncSession, user_id: str) -> model:
        query = select(cls.model).where(cls.model.user_id == user_id)
        return (await db.execute(query)).scalar_one_or_none()

    @classmethod
    async def get_from_group(cls, db: AsyncSession, group_id: str):
        query = select(cls.model).where(cls.model.group_id == group_id)
        return (await db.execute(query)).scalars().all()


student_oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/student_login')


async def verify_student(token: Annotated[str, Depends(student_oauth2_bearer)]):
    try:
        payload = await AuthRepository.decode_token(token)
        expire: int = payload.get('exp')
        if expire <= int(datetime.now().timestamp()):
            raise HTTPException(status_code=401, detail='token expired')

        user_type: str = payload.get('user_type')
        if user_type == 'admin':
            return payload

        mail: str = payload.get('mail')
        if mail and user_type == 'student':
            return payload

        raise HTTPException(status_code=401, detail='Could not validate user.')

    except JWTError:
        raise HTTPException(status_code=401, detail='Could not validate user.')

