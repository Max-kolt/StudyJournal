from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from src.entities.Parents.service import ParentService
from src.entities.Students.service import StudentService
from src.entities.Teachers.service import TeacherService
from database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession

from src.entities.AdminPanel.service import AdminService


auth_router = APIRouter(prefix='/auth', tags=['Authentication'])


@auth_router.post('/manager_login')
async def manager_login(form: Annotated[OAuth2PasswordRequestForm, Depends()], db: AsyncSession = Depends(get_async_session)):
    token = await AdminService.login(db, form)
    return {"access_token": token, "token_type": "bearer"}


@auth_router.post('/teacher_login')
async def teacher_login(form: Annotated[OAuth2PasswordRequestForm, Depends()], db: AsyncSession = Depends(get_async_session)):
    token = await TeacherService.login(db, form)
    return {"access_token": token, "token_type": "bearer"}


@auth_router.post('/student_login')
async def student_login(form: Annotated[OAuth2PasswordRequestForm, Depends()], db: AsyncSession = Depends(get_async_session)):
    token = await StudentService.login(db, form)
    return {"access_token": token, "token_type": "bearer"}


@auth_router.post('/parent_login')
async def parent_login(form: Annotated[OAuth2PasswordRequestForm, Depends()], db: AsyncSession = Depends(get_async_session)):
    token = await ParentService.login(db, form)
    return {"access_token": token, "token_type": "bearer"}
