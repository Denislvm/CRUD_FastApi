import json
from starlette.testclient import TestClient
import pytest
from ..app import app
from ..routes import api


client = TestClient(app)

data = {
    "username": "Kostya",
    "password":"12345",
    "email": "kot@example.com",
}


def test_create_note(create_user, monkeypatch):
    test_response = {"id": 4, "username": "Kostya", "password": "12345", "email": "kot@example.com"}

    async def mock_post():
        return 1

    monkeypatch.setattr(api, "post", mock_post)

    response = create_user.post("/POST/user", data=json.dumps(test_response),)

    assert response.status_code == 201
    assert response.json() == test_response

