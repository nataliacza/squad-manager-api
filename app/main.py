from fastapi import FastAPI

from app.config import settings
from app.core.database import create_db_and_tables
from app.routers.dogs_api import dogs_router
from app.routers.members_api import members_router


def get_application():
    _app = FastAPI(title=settings.PROJECT_NAME,
                   version=settings.PROJECT_VERSION,
                   description=settings.PROJECT_DESCRIPTION,
                   openapi_tags=settings.API_TAGS)

    create_db_and_tables()

    return _app


app = get_application()
app.include_router(members_router)
app.include_router(dogs_router)
