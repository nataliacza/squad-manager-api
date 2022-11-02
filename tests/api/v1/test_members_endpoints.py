import json


def test_create_member(client):
    data = {
        "first_name": "TestName",
        "last_name": "TestSurname",
        "mobile": "12345679",
        "email": "user@example.com"
    }

    response = client.post("/v1/members/", data=json.dumps(data))

    assert response.status_code == 200
    assert response.json()["first_name"] == "TestName"
    assert response.json()["last_name"] == "TestSurname"
