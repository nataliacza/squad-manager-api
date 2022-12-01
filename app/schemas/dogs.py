from datetime import date
from typing import Optional
from uuid import UUID

from pydantic import validator, Field
from sqlmodel import SQLModel

from app.db.models.enums import GenderEnum

# TODO: figure out how to resolve issue with
#  ImportError: cannot import name 'MemberNameIdDto' from partially initialized module 'app.schemas.members'
class MemberInfo(SQLModel):
    id: UUID
    first_name: str
    last_name: str


class DogId(SQLModel):
    id: UUID


class DogName(SQLModel):
    name: str = Field(min_length=2, max_length=30)

    @validator("name")
    def transform(cls, v: str):
        if v is not None:
            return v.title()

    class Config:
        anystr_strip_whitespace = True


class DogDetails(SQLModel):
    breed: Optional[str] = Field(default=None, min_length=2, max_length=40)
    breeder: Optional[str] = Field(default=None, min_length=2, max_length=40)
    gender: Optional[GenderEnum] = None
    dob: Optional[date] = None
    chip: Optional[str] = Field(default=None, min_length=2, max_length=40)

    @validator("dob")
    def future_date(cls, dob):
        today = date.today()
        if dob is not None and dob > today:
            assert False, "provide date from past"
        return dob

    @validator("breed", "breeder")
    def transform(cls, v: str):
        if v is not None:
            return v.title()

    class Config:
        anystr_strip_whitespace = True


class DogIdWithNameDto(DogName, DogId):
    pass


class SaveDogDto(DogDetails, DogName):
    owner_id: UUID


class DogDetailsReadDto(DogDetails, DogName, DogId):
    owner: MemberInfo
