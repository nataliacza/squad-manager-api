from typing import Optional

from pydantic import BaseModel
from sqlmodel import Field

from app.models.enums import GenderEnum


class DogDto(BaseModel):
    id: int
    name: str
    breed: Optional[str] = None
    breeder: Optional[str] = None
    gender: Optional[GenderEnum] = None
    dob: Optional[str] = None
    chip: Optional[str] = None
    owner_id: int = Field(foreign_key="members.id")


class CreateDogDto(BaseModel):
    name: str
    owner_id: int = Field(foreign_key="members.id")
