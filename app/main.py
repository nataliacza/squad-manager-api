from fastapi import FastAPI
from sqlmodel import SQLModel

from app.api.base import api_router
from app.core.config import settings
from app.db.dev_engine import engine, check_db_connected, check_db_disconnected


def include_router(application):
    application.include_router(api_router)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def start_application():
    _app = FastAPI(title=settings.PROJECT_NAME,
                   version=settings.PROJECT_VERSION,
                   description=settings.PROJECT_DESCRIPTION,
                   openapi_tags=settings.API_TAGS)

    include_router(_app)
    create_db_and_tables()
    return _app


app = start_application()


@app.on_event("startup")
async def app_startup():
    await check_db_connected()


@app.on_event("shutdown")
async def app_shutdown():
    await check_db_disconnected()
