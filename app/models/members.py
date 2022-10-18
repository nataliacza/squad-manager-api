from datetime import datetime
from typing import Optional, List

from pydantic import EmailStr
from sqlmodel import SQLModel, Field, Relationship

from app.models.enums import FunctionEnum, InstitutionEnum, CourseEnum


# def generate_uuid():
#     return str(uuid.uuid4())


class Course(SQLModel, table=True):
    __tablename__ = "courses"

    id: Optional[int] = Field(primary_key=True, index=True)
    course_name: CourseEnum
    date: datetime = Field(default=None, nullable=True)
    expires: datetime = Field(default=None, nullable=True)

    member_id: Optional[int] = Field(default=None, foreign_key="members.id")
    member: Optional["Member"] = Relationship(back_populates="courses")


class Member(SQLModel, table=True):
    __tablename__ = "members"

    id: Optional[int] = Field(primary_key=True, index=True)
    first_name: str
    last_name: str
    mobile: str
    email: EmailStr
    function: Optional[FunctionEnum] = Field(default=None, nullable=True)
    institution: Optional[InstitutionEnum] = Field(default=None, nullable=True)

    courses: List[Course] = Relationship(back_populates="member")
