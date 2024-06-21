from src.abstract.base_repo import BaseRepo
from .model import Group


class GroupRepository(BaseRepo):
    model = Group

