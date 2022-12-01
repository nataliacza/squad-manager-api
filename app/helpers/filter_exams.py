from typing import Union

from sqlalchemy.sql.elements import or_
from sqlmodel.sql.expression import select

from app.db.models.core_models import Exam, Dog, Member
from app.db.models.enums import ExamEnum


def filter_query(dog: Union[str, None],
                 member: Union[str, None],
                 exam: Union[ExamEnum, None]) -> select:

    query = select(Exam)
    if all(value is None for value in [dog, member, exam]):
        return query

    if dog:
        query = query.join(Exam.dog).filter(Dog.name.ilike(f"%{dog}%"))

    if member:
        query = query.join(Exam.member).filter(
            or_(Member.first_name.ilike(f"%{member}%"),
                Member.last_name.ilike(f"%{member}%"))
        )

    if exam:
        query = query.where(Exam.type == exam)

    return query
