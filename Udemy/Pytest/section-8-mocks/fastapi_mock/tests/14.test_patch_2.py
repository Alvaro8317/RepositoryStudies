from unittest.mock import patch
from fastapi.testclient import TestClient
from src.app import web_app

client = TestClient(web_app)


# Patch en decorador
# Una vez terminado el test, se cierra el test, mejor practica que patch manual
# El patch en decorador se pasa el primer parámetro, por lo que se recomienda dejar las fixture después
@patch("src.app.retorna_string")
def test_mock_string(mock_string):
    ret_value = "Una cosa en mock"
    mock_string.return_value = ret_value
    response = client.get("/api")
    assert response.json() == ret_value


@patch("src.app.retorna_string", lambda: "Una cosa en mock")
def test_mock_string_2():
    response = client.get("/api")
    assert response.json() == "Una cosa en mock"
