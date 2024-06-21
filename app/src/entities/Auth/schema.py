from typing import Annotated

from fastapi import Depends
from passlib.context import CryptContext
from pydantic import BaseModel

from .repository import verify_auth
from src.entities.AdminPanel.repository import verify_admin
from src.entities.Students.repository import verify_student
from src.entities.Teachers.repository import verify_teacher

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated="auto")

auth_dep = Annotated[dict, Depends(verify_auth)]
student_dep = Annotated[dict, Depends(verify_student)]
teacher_dep = Annotated[dict, Depends(verify_teacher)]
admin_dep = Annotated[dict, Depends(verify_admin)]
