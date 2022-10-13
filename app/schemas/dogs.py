from typing import Optional

from pydantic import BaseModel
from sqlmodel import Field

from app.models.enums import Gender


class DogDto(BaseModel):
    id: int
    name: str
    breed: Optional[str] = None
    gender: Optional[Gender] = None
    dob: Optional[str] = None
    chip: Optional[str] = None
    owner_id: int = Field(foreign_key="members.id")


class CreateDogDto(BaseModel):
    name: str
    owner_id: int = Field(foreign_key="members.id")
