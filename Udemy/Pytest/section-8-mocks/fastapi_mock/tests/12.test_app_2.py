from unittest.mock import patch
import time
import pytest
from fastapi.exceptions import HTTPException
from fastapi.testclient import TestClient
from src.app import web_app

# TestClient permite ejecutar el código dentro del test, es un test de caja blanca del cuál uno conoce la implementación
# Testclient no permite tocar la implementación del endpoint
client = TestClient(web_app)


def test_connection_default():
    response = client.get("/")
    print(response.text)


def test_connection_timeout():
    with patch("src.app.time") as mock:
        mock.sleep.side_effect = HTTPException(status_code=504)
        response = client.get("/timeout")
        print(response)
        print(response.text)
