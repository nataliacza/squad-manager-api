from typing import Generator

import databases
from sqlmodel import create_engine, Session

from app.core.config import settings

POSTGRES_DB = settings.DATABASE_URL
engine = create_engine(POSTGRES_DB, echo=True)


def get_session() -> Generator:
    with Session(engine) as session:
        yield session


async def check_db_connected():
    try:
        database = databases.Database(POSTGRES_DB)
        if not database.is_connected:
            await database.connect()
            await database.execute("SELECT 1")
        print("Database is connected")
    except Exception as e:
        print("There is an issue with database connection, see below traceback:")
        raise e


async def check_db_disconnected():
    try:
        database = databases.Database(POSTGRES_DB)
        if database.is_connected:
            await database.disconnect()
        print("Database is disconnected")
    except Exception as e:
        raise e
