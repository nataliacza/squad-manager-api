from typing import Optional

from pydantic import BaseModel, EmailStr

from app.models.enums import Function, Institution


class MemberDto(BaseModel):
    id: int
    first_name: str
    last_name: str
    mobile: str
    email: EmailStr


class MemberDetailsDto(MemberDto):
    function: Optional[Function] = None
    institution: Optional[Institution] = None


class MemberCreateDto(BaseModel):
    first_name: str
    last_name: str
    mobile: str
    email: EmailStr
