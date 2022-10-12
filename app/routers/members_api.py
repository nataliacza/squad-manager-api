from typing import List

from fastapi import APIRouter

from app.models.members import Member


members_router = APIRouter(prefix="/members",
                           tags=["members"])


@members_router.get(path="/",
                    response_model=List[Member],
                    summary="Get all members",
                    responses={200: {"detail": "Successful operation"},
                               401: {"detail": "Unauthorized"},
                               405: {"detail": "Method Not Allowed"}})
async def get_all_members():
    return {"message": "Hello World!"}
