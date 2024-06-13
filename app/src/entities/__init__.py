from .Users.router import users_router
from .Auth.router import auth_router
from .AdminPanel.router import admin_router
from .Specializations.router import specializations_router
from .Users.model import Base
from .AdminPanel.model import Base
from .Teachers.model import Base
from .Students.model import Base
from .Parents.model import Base
from .Plan.model import Base
from .Specializations.model import Base


all_routers = [auth_router, admin_router, specializations_router]
__all__ = ['Base']
