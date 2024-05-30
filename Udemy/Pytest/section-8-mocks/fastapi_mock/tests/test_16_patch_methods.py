from unittest.mock import patch
from fastapi.testclient import TestClient
from src.app import web_app

client = TestClient(web_app)


def test_mock_string():
    with patch("src.app.Foo.retorna_string_foo", return_value="Prueba") as mock_string:
        response = client.get("/api/v2")
    assert response.json() == "Prueba"
