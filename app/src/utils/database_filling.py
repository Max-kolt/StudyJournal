from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncConnection

from config import ADMIN_MANAGER_USERNAME, ADMIN_MANAGER_PASSWORD
from src.entities.Auth.schema import bcrypt_context


async def database_filling(con: AsyncConnection):
    await con.execute(text(
        f"insert into head_of_department (name, password) values " +
        f"('{ADMIN_MANAGER_USERNAME}', '{bcrypt_context.hash(ADMIN_MANAGER_PASSWORD)}');"
    ))