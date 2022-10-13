from typing import Optional

from pydantic import BaseModel, EmailStr

from app.models.enums import Function, Institution


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
    function: Optional[Function] = None
    institution: Optional[Institution] = None


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
    function: Optional[Function] = None
    institution: Optional[Institution] = None
