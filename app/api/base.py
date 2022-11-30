from fastapi import APIRouter

from app.api.v1 import (members_endpoints, exams_endpoints, dogs_endpoints)

api_router = APIRouter()
api_router.include_router(members_endpoints.router, prefix="/v1/members", tags=["Members"])
api_router.include_router(exams_endpoints.router, prefix="/v1/exams", tags=["Exams"])
api_router.include_router(dogs_endpoints.router, prefix="/v1/dogs", tags=["Dogs"])
