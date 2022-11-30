from sqlmodel import Session

from app.db.dev_engine import engine
from app.db.models.core_models import Course
from app.db.models.enums import CourseEnum


def generate_courses(member_id: int):

    courses_list = [Course(member_id=member_id, course_name=CourseEnum.Kpp),
                    Course(member_id=member_id, course_name=CourseEnum.Badania),
                    Course(member_id=member_id, course_name=CourseEnum.Kurs_podstawowy),
                    Course(member_id=member_id, course_name=CourseEnum.Kurs_przewodnikow),
                    Course(member_id=member_id, course_name=CourseEnum.Kurs_instruktora),
                    Course(member_id=member_id, course_name=CourseEnum.Kurs_egzaminatora),
                    Course(member_id=member_id, course_name=CourseEnum.Kurs_dowodcow),
                    Course(member_id=member_id, course_name=CourseEnum.Kurs_wysokosciowy),
                    Course(member_id=member_id, course_name=CourseEnum.Kurs_smiglowcowy)
                    ]

    with Session(engine) as session:
        session.add_all(courses_list)
        session.commit()
