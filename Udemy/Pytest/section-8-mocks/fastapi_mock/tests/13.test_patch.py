from unittest.mock import patch
from fastapi.testclient import TestClient
from src.app import web_app

client = TestClient(web_app)

# Patch manual
def test_mock_string():
    patcher = patch("src.app.retorna_string")
    # Start devuelve el mock con el que se va a trabajar
    mock_string = patcher.start()
    ret_value = "Una cosa en mock"
    mock_string.return_value = ret_value
    response = client.get("/api")
    print(response.text)
    assert response.json() == ret_value
    # Siempre se debe de cerrar el patch porque si hay varios tests, el patch puede interferir en otros tests
    patcher.stop()
    # Se confirma que el mock se detuvo
    response = client.get("/api")
    assert response.json() == "string"
