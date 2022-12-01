from typing import Optional, List
from uuid import UUID

from pydantic import EmailStr, Field, validator
from sqlmodel import SQLModel

from app.db.models.enums import FunctionEnum, InstitutionEnum
from app.schemas.courses import CourseReadDto
from app.schemas.dogs import DogIdWithName


class MemberIdDto(SQLModel):
    id: UUID


class MemberBaseDto(SQLModel):
    first_name: str = Field(min_length=2, max_length=40)
    last_name: str = Field(min_length=2, max_length=40)
    mobile: str = Field(min_length=9, max_length=11)
    email: EmailStr

    @validator("first_name", "last_name")
    def transform(cls, v: str):
        if v is not None:
            return v.title()

    @validator("mobile")
    def is_digit(cls, v: str):
        assert v.isdigit(), 'must contain digits'
        return v

    class Config:
        anystr_strip_whitespace = True


class MemberDetailsDto(SQLModel):
    function: Optional[FunctionEnum] = None
    institution: Optional[InstitutionEnum] = None


class MemberDogsDto(SQLModel):
    dogs: Optional[List[DogIdWithName]] = None


class MemberCoursesDto(SQLModel):
    courses: List[CourseReadDto]


class MemberListViewDto(MemberCoursesDto, MemberBaseDto, MemberIdDto):
    pass


class MemberDetailsReadDto(MemberCoursesDto, MemberDogsDto, MemberDetailsDto, MemberBaseDto, MemberIdDto):
    pass


class CreateMemberDto(MemberBaseDto):
    pass


class MemberResponseDto(MemberDetailsDto, MemberBaseDto, MemberIdDto):
    pass


class UpdateMemberDetailsDto(MemberDetailsDto, MemberBaseDto):
    pass


class MemberListDto(MemberBaseDto, MemberIdDto):
    pass


class MemberNameDto(MemberIdDto):
    first_name: str
    last_name: str
