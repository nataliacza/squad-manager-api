from typing import List

from fastapi import APIRouter
from pydantic import ValidationError
from sqlmodel import Session, select
from starlette.responses import JSONResponse

from app.core.database import engine
from app.helpers.check_existing_exams import check_exam
from app.models.core_models import Member, Dog, Exam
from app.schemas.exams import SaveExamDto, ExamDetailsDto

exams_router = APIRouter(prefix="/exams",
                         tags=["Exams"])


@exams_router.post(path="/",
                   response_model=ExamDetailsDto,
                   summary="Add new exam",
                   status_code=201,
                   responses={201: {"detail": "Created"},
                              401: {"detail": "Unauthorized"},
                              400: {"detail": "Bad Request"},
                              404: {"detail": "Not Found"},
                              405: {"detail": "Method Not Allowed"}})
async def add_exam(exam_details: SaveExamDto):

    with Session(engine) as session:
        get_member = session.get(Member, exam_details.member_id)
        get_dog = session.get(Dog, exam_details.dog_id)

        if not get_member:
            return JSONResponse(status_code=404, content={"detail": "Member Id Not Found"})

        if not get_dog:
            return JSONResponse(status_code=404, content={"detail": "Dog Id Not Found"})

        already_exist = await check_exam(get_member.id, get_dog.id, exam_details.type)

        if already_exist:
            return JSONResponse(status_code=400, content={"detail": "Exam Already Exist"})

        try:
            new_exam = Exam.from_orm(exam_details)
            session.add(new_exam)
            session.commit()
            session.refresh(new_exam)
            return new_exam

        except ValidationError as error:
            return error


@exams_router.get(path="/{exam_id}",
                  response_model=ExamDetailsDto,
                  summary="Get exam by id",
                  status_code=200,
                  responses={200: {"detail": "Successful operation"},
                             401: {"detail": "Unauthorized"},
                             404: {"detail": "Not Found"},
                             405: {"detail": "Method Not Allowed"}})
async def get_exam_by_id(exam_id: int):

    with Session(engine) as session:
        get_exam = session.get(Exam, exam_id)

        if get_exam:
            return get_exam

        return JSONResponse(status_code=404, content={"detail": "Id Not Found"})


@exams_router.get(path="/",
                  response_model=List[ExamDetailsDto],
                  summary="Get all exams",
                  status_code=200,
                  responses={200: {"detail": "Successful operation"},
                             401: {"detail": "Unauthorized"},
                             405: {"detail": "Method Not Allowed"}})
async def get_all_exams():

    with Session(engine) as session:
        exams = session.exec(select(Exam)).all()
        return exams
