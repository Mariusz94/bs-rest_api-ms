import pytest

from server import app
import json


@pytest.fixture
def client():
    """
    Fixture tworzący klienta aplikacji Flask do testów.
    """
    with app.test_client() as client:
        yield client


def test_welcome_endpoint(client):
    """
    Testuje endpoint GET o ścieżce "/".
    """
    response = client.get("/")
    assert response.status_code == 200
    data = json.loads(response.data.decode("utf-8"))
    assert "info" in data
    assert data["info"] == "server works"


def test_login_endpoint(client):
    """
    Testuje endpoint POST o ścieżce "/login".
    """
    login_data = {
        "login": "7654",
        "password": "pass_1",
    }
    data = json.dumps(login_data)
    response = client.post("/login", json=login_data, content_type="application/json")
    assert response.status_code == 200
    data = json.loads(response.data.decode("utf-8"))
    assert "access_token" in data
    assert "refresh_token" in data
