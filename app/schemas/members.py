from datetime import date
from typing import Optional, List
from uuid import UUID

from pydantic import EmailStr, Field, validator
from sqlmodel import SQLModel

from app.db.models.enums import FunctionEnum, InstitutionEnum
from app.schemas.courses import CourseReadDto
from app.schemas.dogs import DogIdWithNameDto


class MemberId(SQLModel):
    id: UUID


class MemberName(SQLModel):
    first_name: str
    last_name: str

    @validator("first_name", "last_name")
    def transform(cls, v: str):
        if v is not None:
            return v.title()

    class Config:
        anystr_strip_whitespace = True


class MemberContact(SQLModel):
    mobile: str = Field(min_length=9, max_length=11)
    email: EmailStr

    @validator("mobile")
    def is_digit(cls, v: str):
        assert v.isdigit(), 'must contain digits'
        return v

    class Config:
        anystr_strip_whitespace = True


class MemberDetails(SQLModel):
    function: Optional[FunctionEnum] = None
    institution: Optional[InstitutionEnum] = None


class MemberDogs(SQLModel):
    dogs: Optional[List[DogIdWithNameDto]] = None


class MemberCourses(SQLModel):
    courses: List[CourseReadDto]


class MemberListViewDto(MemberCourses, MemberContact, MemberName, MemberId):
    pass


class MemberDetailsReadDto(MemberCourses, MemberDogs, MemberDetails, MemberContact, MemberName, MemberId):
    pass


class CreateMemberDto(MemberContact, MemberName):
    pass


class MemberResponseDto(MemberDetails, MemberContact, MemberName, MemberId):
    pass


class UpdateMemberDetailsDto(MemberDetails, MemberContact, MemberName):
    pass


class MemberNameIdDto(MemberName, MemberId):
    pass
