from sqlmodel import Session, select

from app.core.database import engine
from app.models.core_models import Exam
from app.models.enums import ExamEnum


async def check_exam(member: int, dog: int, exam: ExamEnum) -> bool:

    with Session(engine) as session:
        query = select(Exam).where(Exam.member_id == member, Exam.dog_id == dog, Exam.type == exam)
        statement = session.exec(query).first()

    if statement:
        return True
    return False
