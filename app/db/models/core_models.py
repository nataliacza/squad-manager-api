from datetime import date
from typing import Optional, List

from pydantic import EmailStr
from sqlmodel import SQLModel, Field, Relationship

from app.db.models.enums import FunctionEnum, InstitutionEnum, CourseEnum, GenderEnum, ExamEnum


class Member(SQLModel, table=True):
    __tablename__ = "members"

    id: Optional[int] = Field(primary_key=True, index=True)
    first_name: str
    last_name: str
    mobile: str
    email: EmailStr
    function: Optional[FunctionEnum] = Field(default=None, nullable=True)
    institution: Optional[InstitutionEnum] = Field(default=None, nullable=True)

    courses: List["Course"] = Relationship(back_populates="member",
                                           sa_relationship_kwargs={"lazy": "selectin",
                                                                   "cascade": "all, delete , delete-orphan"})
    dogs: List["Dog"] = Relationship(back_populates="owner",
                                     sa_relationship_kwargs={"lazy": "selectin"})
    exams: List["Exam"] = Relationship(back_populates="member",
                                       sa_relationship_kwargs={"lazy": "selectin",
                                                               "cascade": "all, delete , delete-orphan"})


class Course(SQLModel, table=True):
    __tablename__ = "courses"

    id: Optional[int] = Field(primary_key=True, index=True)
    course_name: CourseEnum
    date_from: date = Field(default=None, nullable=True)
    expires: date = Field(default=None, nullable=True)

    member_id: int = Field(foreign_key="members.id")
    member: Member = Relationship(back_populates="courses",
                                  sa_relationship_kwargs={"lazy": "selectin"})


class Dog(SQLModel, table=True):
    __tablename__ = "dogs"

    id: Optional[int] = Field(primary_key=True, index=True)
    name: str
    breed: Optional[str] = None
    breeder: Optional[str] = None
    gender: Optional[GenderEnum] = None
    dob: Optional[date] = None
    chip: Optional[str] = None

    owner_id: int = Field(foreign_key="members.id")
    owner: Member = Relationship(back_populates="dogs",
                                 sa_relationship_kwargs={"lazy": "selectin"})

    exams: List["Exam"] = Relationship(back_populates="dog",
                                       sa_relationship_kwargs={"lazy": "selectin",
                                                               "cascade": "all, delete , delete-orphan"})


class Exam(SQLModel, table=True):
    __tablename__ = "exams"

    id: Optional[int] = Field(primary_key=True, index=True)
    type: ExamEnum
    member_id: int = Field(foreign_key="members.id")
    dog_id: int = Field(foreign_key="dogs.id")
    date_from: date
    expires: date

    member: Member = Relationship(back_populates="exams",
                                  sa_relationship_kwargs={"lazy": "selectin"})
    dog: Dog = Relationship(back_populates="exams",
                            sa_relationship_kwargs={"lazy": "selectin"})
