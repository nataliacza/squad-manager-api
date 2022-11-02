import pytest
from sqlmodel import Session
from starlette.testclient import TestClient

from app.db.dev_engine import engine
from app.db.models.core_models import Member
from app.main import app


@pytest.fixture()
def client():
    return TestClient(app)


def delete_member(member_id: int):

    with Session(engine) as session:
        get_member = session.get(Member, member_id)
        session.delete(get_member)
        session.commit()
