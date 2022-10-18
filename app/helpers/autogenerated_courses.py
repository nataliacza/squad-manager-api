from app.core.database import engine
from sqlmodel import Session

from app.models.enums import CourseEnum
from app.models.members import Course


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
