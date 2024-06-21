
from .Auth.router import auth_router
from .AdminPanel.router import admin_router
from .Specializations.router import specializations_router
from .Plan.router import plan_router
from .Groups.reouter import group_router
from .Users.router import user_router
from .Teachers.router import teacher_router
from .Students.router import student_router
from .Timetable.router import timetable_router

from .Plan.model import Base
from .Specializations.model import Base
from .Groups.model import Base
from .Timetable.model import Base
from .Users.model import Base
from .AdminPanel.model import Base
from .Teachers.model import Base
from .Students.model import Base
# from .Parents.model import Base


all_routers = [auth_router, admin_router, user_router, plan_router, specializations_router, group_router, teacher_router, timetable_router, student_router]
__all__ = ['Base']
