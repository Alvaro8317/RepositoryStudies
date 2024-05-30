from unittest.mock import patch
from fastapi.testclient import TestClient
from src.app import Foo, web_app

client = TestClient(web_app)


def test_mock_string():
    with patch.object(target=Foo, attribute="retorna_string_foo", return_value="Prueba object"):
        response = client.get("/api/v2")
    assert response.json() == "Prueba object"
