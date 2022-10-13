from datetime import datetime
from typing import Optional

from pydantic import EmailStr
from sqlmodel import SQLModel, Field

from app.models.enums import Function, Institution, Course


# def generate_uuid():
#     return str(uuid.uuid4())


class Member(SQLModel, table=True):
    __tablename__ = "members"

    id: Optional[int] = Field(primary_key=True, index=True)
    first_name: str
    last_name: str
    mobile: str
    email: EmailStr
    function: Optional[Function] = Field(default=None, nullable=True)
    institution: Optional[Institution] = Field(default=None, nullable=True)
    is_active: bool = Field(default=True, nullable=False)


class Training(SQLModel, table=True):
    __tablename__ = "trainings"

    id: Optional[int] = Field(primary_key=True, index=True)
    member_id: int = Field(foreign_key="members.id")
    course_name: Course
    date: datetime
    expires: datetime
