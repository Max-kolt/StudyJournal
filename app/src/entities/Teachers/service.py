from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from .model import Teacher
from .repository import TeacherRepository
from .schema import TeacherSchema
from src.entities.Auth.schema import bcrypt_context
from src.entities.Auth.repository import AuthRepository
from src.entities.Users.repository import UserRepository
from fastapi import HTTPException

from src.entities.Users.schema import UserSchema
from src.entities.Users.service import UserService
from ..Specializations.repository import SpecializationsRepository


class TeacherService:
    @staticmethod
    async def login(db: AsyncSession, login: OAuth2PasswordRequestForm):
        user = await UserRepository.get_by_mail(db, login.username)
        is_teacher = await TeacherRepository.get_by_user_id(db, user.id)

        if is_teacher and user:
            if bcrypt_context.verify(login.password, user.account[0].password):
                return (
                    AuthRepository.create_token(data={'mail': login.username, 'user_type': 'teacher'}),
                    {'id': user.id, 'mail': user.mail, 'username': f'{user.lname} {user.fname[0]}.' }
                )
        raise HTTPException(status_code=400, detail='Name or password not valid')

    @staticmethod
    async def create_teacher_user(db: AsyncSession, data: TeacherSchema):
        verify = await UserRepository.get_by_mail(db, data.mail)
        if verify:
            raise HTTPException(status_code=400, detail='Mail already taken')
        verify = await SpecializationsRepository.get_by_id(db, data.specialization_id)
        if not verify:
            raise HTTPException(status_code=400, detail='Specialization not valid')

        user_data = UserSchema(
            fname=data.fname,
            lname=data.lname,
            mname=data.mname,
            mail=data.mail,
            phone=data.phone,
            gender=data.gender,
        )
        user_model = await UserService.create_user(db, user_data)
        await TeacherRepository.create(
            db, user_id=user_model.id, specialization_id=data.specialization_id,
            education=data.education, category=data.category
        )
        teacher_model: Teacher = await TeacherRepository.get_by_user_id(db, model_id=user_model.id)
        return teacher_model
