from datetime import date
from uuid import UUID

from pydantic import validator
from sqlmodel import SQLModel

from app.db.models.enums import ExamEnum


class ExamIdDto(SQLModel):
    id: UUID


class ExamBaseDto(SQLModel):
    type: ExamEnum
    member_id: UUID
    dog_id: UUID


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
