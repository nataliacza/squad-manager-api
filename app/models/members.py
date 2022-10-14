from datetime import datetime
from typing import Optional

from pydantic import EmailStr
from sqlmodel import SQLModel, Field

from app.models.enums import FunctionEnum, InstitutionEnum, CourseEnum


# def generate_uuid():
#     return str(uuid.uuid4())


class Member(SQLModel, table=True):
    __tablename__ = "members"

    id: Optional[int] = Field(primary_key=True, index=True)
    first_name: str
    last_name: str
    mobile: str
    email: EmailStr
    function: Optional[FunctionEnum] = Field(default=None, nullable=True)
    institution: Optional[InstitutionEnum] = Field(default=None, nullable=True)


class Course(SQLModel, table=True):
    __tablename__ = "courses"

    id: Optional[int] = Field(primary_key=True, index=True)
    member_id: int = Field(foreign_key="members.id")
    course_name: CourseEnum
    date: datetime
    expires: datetime
