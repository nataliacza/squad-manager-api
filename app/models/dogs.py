from typing import Optional

from sqlmodel import SQLModel, Field

from app.models.enums import Gender


class Dogs(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True, nullable=False)
    name: str = Field(nullable=False)
    breed: Optional[str] = Field(default=None)
    gender: Optional[Gender] = Field(default=None)
    dob: Optional[str] = Field(default=None)
    chip: Optional[str] = Field(default=None)
    owner_id: int = Field(foreign_key="member.id")


class DogsExams(SQLModel, table=True):
    pass
