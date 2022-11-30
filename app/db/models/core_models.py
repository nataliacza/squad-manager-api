from datetime import date
from typing import Optional, List
from uuid import UUID, uuid4

from pydantic import EmailStr
from sqlmodel import Field, SQLModel, Relationship

from app.db.models.enums import FunctionEnum, InstitutionEnum, ExamEnum, GenderEnum, CourseEnum


class Member(SQLModel, table=True):
    __tablename__ = "members"

    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True, nullable=False)
    first_name: str = Field(min_length=2, max_length=40)
    last_name: str = Field(min_length=2, max_length=40)
    mobile: str = Field(min_length=9, max_length=11)
    email: EmailStr
    function: Optional[FunctionEnum] = Field(default=None, nullable=True)
    institution: Optional[InstitutionEnum] = Field(default=None, nullable=True)

    courses: List["Course"] = Relationship(back_populates="member",
                                           sa_relationship_kwargs={"lazy": "selectin",
                                                                   "cascade": "all, delete, delete-orphan"})
    dogs: List["Dog"] = Relationship(back_populates="owner",
                                     sa_relationship_kwargs={"lazy": "selectin"})
    exams: List["Exam"] = Relationship(back_populates="member",
                                       sa_relationship_kwargs={"lazy": "selectin",
                                                               "cascade": "all, delete, delete-orphan"})


class Exam(SQLModel, table=True):
    __tablename__ = "exams"

    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True, nullable=False)
    type: ExamEnum
    member_id: UUID = Field(foreign_key="members.id")
    dog_id: UUID = Field(foreign_key="dogs.id")
    date_from: date
    expires: date

    member: "Member" = Relationship(back_populates="exams",
                                    sa_relationship_kwargs={"lazy": "selectin"})
    dog: "Dog" = Relationship(back_populates="exams",
                              sa_relationship_kwargs={"lazy": "selectin"})


class Dog(SQLModel, table=True):
    __tablename__ = "dogs"

    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True, nullable=False)
    name: str
    breed: Optional[str] = None
    breeder: Optional[str] = None
    gender: Optional[GenderEnum] = None
    dob: Optional[date] = None
    chip: Optional[str] = None

    owner_id: UUID = Field(foreign_key="members.id")
    owner: "Member" = Relationship(back_populates="dogs",
                                   sa_relationship_kwargs={"lazy": "selectin"})

    exams: List["Exam"] = Relationship(back_populates="dog",
                                       sa_relationship_kwargs={"lazy": "selectin",
                                                               "cascade": "all, delete, delete-orphan"})


class Course(SQLModel, table=True):
    __tablename__ = "courses"

    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True, nullable=False)
    course_name: CourseEnum
    date_from: date = Field(default=None, nullable=True)
    expires: date = Field(default=None, nullable=True)

    member_id: UUID = Field(foreign_key="members.id")
    member: "Member" = Relationship(back_populates="courses",
                                    sa_relationship_kwargs={"lazy": "selectin"})
