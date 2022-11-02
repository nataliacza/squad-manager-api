import databases
from sqlmodel import create_engine

from app.core.config import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# TODO: create session generator


async def check_db_connected():
    try:
        database = databases.Database(SQLALCHEMY_DATABASE_URL)
        if not database.is_connected:
            await database.connect()
            await database.execute("SELECT 1")
        print("Database is connected")
    except Exception as e:
        print("There is an issue with database connection, see below traceback:")
        raise e


async def check_db_disconnected():
    try:
        database = databases.Database(SQLALCHEMY_DATABASE_URL)
        if database.is_connected:
            await database.disconnect()
        print("Database is disconnected")
    except Exception as e:
        raise e
