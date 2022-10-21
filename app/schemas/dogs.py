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


class DogIdWithName(DogNameDto, DogIdDto):
    pass


class SaveDogDto(DogOwnerDto, DogDetailsDto, DogNameDto):
    pass


class DogDetailsReadDto(DogOwnerDto, DogDetailsDto, DogNameDto, DogIdDto):
    pass




