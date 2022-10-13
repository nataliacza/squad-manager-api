from typing import List

from fastapi import APIRouter
from pydantic import ValidationError
from sqlmodel import Session, select
from starlette.responses import JSONResponse

from app.core.database import engine
from app.models.members import Member
from app.schemas.members import MemberDto, MemberDetailsDto, MemberCreateDto

members_router = APIRouter(prefix="/members",
                           tags=["Members"])


@members_router.post(path="/",
                     response_model=MemberDto,
                     summary="Add new member",
                     status_code=201,
                     responses={201: {"detail": "Created"},
                                401: {"detail": "Unauthorized"},
                                400: {"detail": "Bad Request"},
                                405: {"detail": "Method Not Allowed"}})
async def add_member(member_details: MemberCreateDto):

    with Session(engine) as session:
        try:
            # new_member = Member.from_orm(member_details)
            new_member = Member(**member_details.dict())
            session.add(new_member)
            session.commit()
            session.refresh(new_member)
            return new_member

        except ValidationError as error:
            return error


@members_router.get(path="/",
                    response_model=List[MemberDto],
                    summary="Get all members",
                    status_code=200,
                    responses={200: {"detail": "Successful operation"},
                               401: {"detail": "Unauthorized"},
                               405: {"detail": "Method Not Allowed"}})
async def get_all_members():

    with Session(engine) as session:
        members = session.exec(select(Member)).all()
        return members


@members_router.get(path="/{id}",
                    response_model=MemberDto,
                    summary="Get member basic info",
                    status_code=200,
                    responses={200: {"detail": "Successful operation"},
                               401: {"detail": "Unauthorized"},
                               404: {"detail": "Not Found"},
                               405: {"detail": "Method Not Allowed"}})
async def get_member_by_id(id: int):

    with Session(engine) as session:
        get_member = session.get(Member, id)

        if get_member:
            return get_member

        return JSONResponse(status_code=404, content={"detail": f"Id Not Found"})


@members_router.get(path="/{id}/details",
                    response_model=MemberDetailsDto,
                    summary="Get member details",
                    status_code=200,
                    responses={200: {"detail": "Successful operation"},
                               401: {"detail": "Unauthorized"},
                               404: {"detail": "Not Found"},
                               405: {"detail": "Method Not Allowed"}})
async def get_member_details(id: int):

    with Session(engine) as session:
        get_member = session.get(Member, id)

        if get_member:
            return get_member

        return JSONResponse(status_code=404, content={"detail": f"Id Not Found"})
