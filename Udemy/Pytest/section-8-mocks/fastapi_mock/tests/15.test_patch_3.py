from unittest.mock import patch
from fastapi.testclient import TestClient
from src.app import web_app

client = TestClient(web_app)


# Patch con context man
# Más usado porque se define cuando inicia y cuando termina
def test_mock_string():
    with patch("src.app.retorna_string", return_value="Prueba") as mock_string:
        response = client.get("/api")
    assert response.json() == "Prueba"
