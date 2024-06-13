import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from sqlalchemy import text

from config import ADMIN_MANAGER_PASSWORD, ADMIN_MANAGER_USERNAME
from database import engine
from src import all_routers, Base
from src.utils import database_filling

app = FastAPI(root_path='/api/v1')
logger.add('logger.log', rotation="500 MB", compression="gz", level="DEBUG", diagnose=False, backtrace=False)

for router in all_routers:
    app.include_router(router)


origins = [
    "http://127.0.0.1:8080",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event('startup')
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        print('delete all tables')
        await conn.run_sync(Base.metadata.create_all)
        print('create all tables')
        try:
            await database_filling(conn)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
