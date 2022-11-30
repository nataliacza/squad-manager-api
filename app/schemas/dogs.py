from datetime import date
from typing import Optional
from uuid import UUID

from pydantic import validator, Field
from sqlmodel import SQLModel

from app.db.models.enums import GenderEnum


class DogIdDto(SQLModel):
    id: UUID


class DogNameDto(SQLModel):
    name: str = Field(min_length=2, max_length=30)

    @validator("name")
    def transform(cls, v: str):
        return v.title()

    class Config:
        anystr_strip_whitespace = True


class DogDetailsDto(SQLModel):
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
        return v.title()

    class Config:
        anystr_strip_whitespace = True


class DogOwnerDto(SQLModel):
    owner_id: UUID


class DogIdWithName(DogNameDto, DogIdDto):
    pass


class SaveDogDto(DogOwnerDto, DogDetailsDto, DogNameDto):
    pass


class DogDetailsReadDto(DogOwnerDto, DogDetailsDto, DogNameDto, DogIdDto):
    pass
