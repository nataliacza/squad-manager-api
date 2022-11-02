import json

from sqlmodel import Session

from app.db.dev_engine import engine
from app.db.models.core_models import Member
from tests.conftest import delete_member


def test_add_member_when_new_member_is_created_returns_201_with_response_data(client):
    data = {
        "first_name": "TestName",
        "last_name": "TestSurname",
        "mobile": "12345679",
        "email": "user@example.com"
    }

    response = client.post("/v1/members/", data=json.dumps(data))

    response_data = response.json()

    assert response.status_code == 201
    assert response_data["id"] is not None
    assert response_data["first_name"] == "TestName"
    assert response_data["last_name"] == "TestSurname"
    assert response_data["mobile"] == "12345679"
    assert response_data["email"] == "user@example.com"
    assert response_data["function"] is None
    assert response_data["institution"] is None

    delete_member(response_data["id"])


def test_when_new_member_is_added_9_courses_are_created(client):
    data = {
        "first_name": "TestName",
        "last_name": "TestSurname",
        "mobile": "12345679",
        "email": "user@example.com"
    }

    response = client.post("/v1/members/", data=json.dumps(data))

    response_data = response.json()

    with Session(engine) as session:
        get_member = session.get(Member, response_data["id"])

    assert get_member is not None
    assert len(get_member.courses) == 9

    delete_member(response_data["id"])


def test_when_first_name_is_not_provided_returns_422(client):
    data = {
        "first_name": None,
        "last_name": "TestSurname",
        "mobile": "12345679",
        "email": "user@example.com"
    }

    response = client.post("/v1/members/", data=json.dumps(data))

    assert response.status_code == 422


def test_when_last_name_is_not_provided_returns_422(client):
    data = {
        "first_name": "TestName",
        "last_name": None,
        "mobile": "12345679",
        "email": "user@example.com"
    }

    response = client.post("/v1/members/", data=json.dumps(data))

    assert response.status_code == 422


def test_when_mobile_is_not_provided_returns_422(client):
    data = {
        "first_name": "TestName",
        "last_name": "TestSurname",
        "mobile": None,
        "email": "user@example.com"
    }

    response = client.post("/v1/members/", data=json.dumps(data))

    assert response.status_code == 422


def test_when_email_is_not_provided_returns_422(client):
    data = {
        "first_name": "TestName",
        "last_name": "TestSurname",
        "mobile": "12345679",
        "email": None
    }

    response = client.post("/v1/members/", data=json.dumps(data))

    assert response.status_code == 422
