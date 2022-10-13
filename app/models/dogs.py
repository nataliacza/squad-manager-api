from typing import Optional

from sqlmodel import SQLModel, Field

from app.models.enums import Gender


class Dog(SQLModel, table=True):
    __tablename__ = "dogs"

    id: Optional[int] = Field(primary_key=True, index=True)
    name: str
    breed: Optional[str] = None
    gender: Optional[Gender] = None
    dob: Optional[str] = None
    chip: Optional[str] = None
    owner_id: int = Field(foreign_key="members.id")


# class DogsExams(SQLModel, table=True):
#     pass
