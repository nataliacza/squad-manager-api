from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends
from pydantic import ValidationError
from sqlmodel import Session, select
from starlette.responses import JSONResponse

from app.db.dev_engine import get_session
from app.db.models.core_models import Member, Exam, Dog
from app.db.models.enums import ExamEnum
from app.helpers.check_existing_exams import check_exam
from app.helpers.filter_exams import filter_query
from app.schemas.exams import (ExamDetailsDto, SaveExamDto, UpdateExamDateDto)


exam_router = APIRouter()


@exam_router.post(path="/",
                  response_model=ExamDetailsDto,
                  summary="Add new exam",
                  status_code=201,
                  responses={201: {"description": "Created"},
                             401: {"description": "Unauthorized"},
                             400: {"description": "Bad Request"},
                             404: {"description": "Not Found"},
                             405: {"description": "Method Not Allowed"}})
async def add_exam(exam_details: SaveExamDto, session: Session = Depends(get_session)):
    get_member = session.get(Member, exam_details.member_id)
    get_dog = session.get(Dog, exam_details.dog_id)

    if not get_member:
        return JSONResponse(status_code=404, content={"description": "Member Id Not Found"})

    if not get_dog:
        return JSONResponse(status_code=404, content={"description": "Dog Id Not Found"})

    already_exist = await check_exam(get_member.id, get_dog.id, exam_details.type)

    if already_exist:
        return JSONResponse(status_code=400, content={"description": "Exam Already Exist"})

    try:
        new_exam = Exam.from_orm(exam_details)
        session.add(new_exam)
        session.commit()
        session.refresh(new_exam)
        return new_exam

    except ValidationError as error:
        return error


@exam_router.get(path="/{exam_id}",
                 response_model=ExamDetailsDto,
                 summary="Get exam by id",
                 status_code=200,
                 responses={200: {"description": "Successful operation"},
                            401: {"description": "Unauthorized"},
                            404: {"description": "Not Found"},
                            405: {"description": "Method Not Allowed"}})
async def get_exam_by_id(exam_id: UUID, session: Session = Depends(get_session)):
    get_exam = session.get(Exam, exam_id)

    if get_exam:
        return get_exam

    return JSONResponse(status_code=404, content={"detail": "Id Not Found"})


@exam_router.get(path="/",
                 response_model=List[ExamDetailsDto],
                 summary="Get all exams",
                 description="Returns list of all exams. Possible to search by dog name,\
                 member name and exam type simultaneously.",
                 status_code=200,
                 responses={200: {"description": "Successful operation"},
                            401: {"description": "Unauthorized"},
                            405: {"description": "Method Not Allowed"}})
async def get_all_exams(*, dog_name: str = None, member_name: str = None, exam_type: ExamEnum = None,
                        session: Session = Depends(get_session)):

    query = filter_query(dog_name, member_name, exam_type)
    exams = session.exec(query).all()
    return exams


@exam_router.patch(path="/{exam_id}",
                   response_model=ExamDetailsDto,
                   summary="Update exam",
                   status_code=200,
                   responses={200: {"description": "Successful operation"},
                              400: {"description": "Bad Request"},
                              401: {"description": "Unauthorized"},
                              405: {"description": "Method Not Allowed"}})
async def update_exam_date(*, exam_id: UUID, update_exam: UpdateExamDateDto,
                           session: Session = Depends(get_session)):
    get_exam = session.exec(select(Exam).where(Exam.id == exam_id)).first()

    if get_exam:
        try:
            new_data = update_exam.dict(exclude_unset=True)
            for key, value in new_data.items():
                setattr(get_exam, key, value)
            session.add(get_exam)
            session.commit()
            session.refresh(get_exam)

            return get_exam

        except ValidationError as error:
            return error

    return JSONResponse(status_code=404, content={"description": "Id Not Found"})


@exam_router.delete(path="/{exam_id}",
                    summary="Delete exam",
                    status_code=204,
                    responses={204: {"description": "No content"},
                               401: {"description": "Unauthorized"},
                               404: {"description": "Not Found"},
                               405: {"description": "Method Not Allowed"}})
async def delete_exam(exam_id: UUID, session: Session = Depends(get_session)):
    get_exam = session.get(Exam, exam_id)

    if get_exam:
        session.delete(get_exam)
        session.commit()
        return {}

    return JSONResponse(status_code=404, content={"description": "Id Not Found"})
