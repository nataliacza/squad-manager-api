from datetime import date
from typing import Optional

from pydantic import validator
from sqlmodel import SQLModel

from app.models.enums import GenderEnum


class DogIdDto(SQLModel):
    id: int


class DogNameDto(SQLModel):
    name: str


class DogDetailsDto(SQLModel):
    breed: Optional[str] = None
    breeder: Optional[str] = None
    gender: Optional[GenderEnum] = None
    dob: Optional[date] = None
    chip: Optional[str] = None

    @validator("dob")
    def future_date(cls, dob):
        today = date.today()
        if dob is not None and dob > today:
            assert False, "provide date from past"
        return dob


class DogOwnerDto(SQLModel):
    owner_id: int


class DogIdWithName(DogNameDto, DogIdDto):
    pass


class SaveDogDto(DogOwnerDto, DogDetailsDto, DogNameDto):
    pass


class DogDetailsReadDto(DogOwnerDto, DogDetailsDto, DogNameDto, DogIdDto):
    pass




