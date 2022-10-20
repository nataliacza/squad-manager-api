from typing import Optional, List

from pydantic import EmailStr
from sqlmodel import SQLModel

from app.models.enums import FunctionEnum, InstitutionEnum
from app.schemas.courses import CourseReadDto, CourseBaseDto
from app.schemas.dogs import DogIdWithName


class MemberIdDto(SQLModel):
    id: int


class MemberBaseDto(SQLModel):
    first_name: str
    last_name: str
    mobile: str
    email: EmailStr


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


class CreateMemberResponseDto(MemberDetailsDto, MemberBaseDto, MemberIdDto):
    pass


class UpdateMemberDetailsDto(MemberDetailsDto, MemberBaseDto):
    pass


class UpdateMemberDetailsResponseDto(MemberDetailsDto, MemberBaseDto, MemberIdDto):
    pass


class MemberListDto(MemberBaseDto, MemberIdDto):
    pass
