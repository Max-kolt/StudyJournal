from typing import Annotated

from fastapi import Depends
from pydantic import BaseModel

from .repository import verify_admin


class AdminSchema(BaseModel):
    name: str
    password: str | None


admin_dep = Annotated[dict, Depends(verify_admin)]
