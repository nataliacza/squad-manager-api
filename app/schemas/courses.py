from datetime import date
from typing import Optional
from uuid import UUID

from pydantic import validator
from sqlmodel import SQLModel

from app.db.models.enums import CourseEnum


class CourseIdDto(SQLModel):
    id: UUID


class CourseNameDto(SQLModel):
    course_name: CourseEnum


class CourseDetailsDto(SQLModel):
    date_from: Optional[date] = None
    expires: Optional[date] = None

    @validator("date_from")
    def future_date(cls, date_from):
        today = date.today()
        if date_from is not None and date_from > today:
            assert False, "provide date from past"
        return date_from


class CourseReadDto(CourseDetailsDto, CourseNameDto, CourseIdDto):
    pass


class UpdateCourseDto(CourseDetailsDto):
    pass
