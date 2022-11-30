from fastapi import FastAPI
from sqlmodel import SQLModel

from app.api.v1 import members_endpoints, exams_endpoints, dogs_endpoints
from app.config import settings
from app.db.dev_engine import engine, check_db_connected, check_db_disconnected


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def start_application():
    _app = FastAPI(title=settings.PROJECT_NAME,
                   version=settings.PROJECT_VERSION,
                   description=settings.PROJECT_DESCRIPTION,
                   openapi_tags=settings.API_TAGS)

    _app.include_router(members_endpoints.member_router, prefix="/v1/members", tags=["Members"])
    _app.include_router(exams_endpoints.exam_router, prefix="/v1/exams", tags=["Exams"])
    _app.include_router(dogs_endpoints.dog_router, prefix="/v1/dogs", tags=["Dogs"])

    create_db_and_tables()
    return _app


app = start_application()


@app.on_event("startup")
async def app_startup():
    await check_db_connected()


@app.on_event("shutdown")
async def app_shutdown():
    await check_db_disconnected()
