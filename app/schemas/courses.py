from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel

from app.models.enums import CourseEnum


class CourseIdDto(SQLModel):
    id: int


class CourseBaseDto(SQLModel):
    course_name: CourseEnum
    date: Optional[datetime] = None
    expires: Optional[datetime] = None


class CourseReadDto(CourseBaseDto, CourseIdDto):
    pass
