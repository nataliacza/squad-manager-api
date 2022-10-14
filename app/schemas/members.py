from typing import Optional

from pydantic import BaseModel, EmailStr

from app.models.enums import FunctionEnum, InstitutionEnum


class MemberDto(BaseModel):
    id: int
    first_name: str
    last_name: str
    mobile: str
    email: EmailStr


class MemberDetailsDto(BaseModel):
    id: int
    first_name: str
    last_name: str
    mobile: str
    email: EmailStr
    function: Optional[FunctionEnum] = None
    institution: Optional[InstitutionEnum] = None


class CreateMemberDto(BaseModel):
    first_name: str
    last_name: str
    mobile: str
    email: EmailStr


class UpdateMemberDetailsDto(BaseModel):
    first_name: str
    last_name: str
    mobile: str
    email: EmailStr
    function: Optional[FunctionEnum] = None
    institution: Optional[InstitutionEnum] = None
