import uuid
from datetime import datetime
from typing import Optional

from pydantic import EmailStr
from sqlmodel import SQLModel, Field

from app.models.enums import Function, Institution, Course


# def generate_uuid():
#     return str(uuid.uuid4())


class Member(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True, nullable=False)
    first_name: str = Field(nullable=False)
    last_name: str = Field(nullable=False)
    mobile: str = Field(nullable=False)
    email: EmailStr = Field(nullable=False)
    function: Optional[Function] = Field(nullable=True)
    institution: Optional[Institution] = Field(nullable=True)
    is_active: bool = Field(default=True, nullable=False)


class MemberCourse(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True, nullable=False)
    member_id: int = Field(foreign_key="member.id", nullable=False)
    course: Course = Field(nullable=False)
    date: datetime = Field(nullable=False)
    expires: datetime = Field(nullable=False)
