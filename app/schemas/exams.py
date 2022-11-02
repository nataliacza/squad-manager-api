from datetime import date

from pydantic import validator
from sqlmodel import SQLModel

from app.db.models.enums import ExamEnum


class ExamIdDto(SQLModel):
    id: int


class ExamBaseDto(SQLModel):
    type: ExamEnum
    member_id: int
    dog_id: int


class ExamDateDto(SQLModel):
    date_from: date
    expires: date

    @validator("date_from")
    def future_date(cls, date_from):
        today = date.today()
        if date_from is not None and date_from > today:
            assert False, "provide date from past"
        return date_from


class SaveExamDto(ExamDateDto, ExamBaseDto):
    pass


class ExamDetailsDto(ExamDateDto, ExamBaseDto, ExamIdDto):
    pass


class UpdateExamDateDto(ExamDateDto):
    pass
