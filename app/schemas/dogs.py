from datetime import datetime
from typing import Optional

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
    dob: Optional[datetime] = None
    chip: Optional[str] = None


class DogOwnerDto(SQLModel):
    owner_id: int


# class DogOwnerNameDto(SQLModel):
#     owner_first_name: str
#     owner_last_name: str


class DogIdWithName(DogNameDto, DogIdDto):
    pass


class CreateDogDto(SQLModel):
    name: str
    owner_id: int


class DogDetailsReadDto(DogOwnerDto, DogDetailsDto, DogNameDto, DogIdDto):
    pass
    # add owner first + last name??




