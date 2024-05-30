from unittest.mock import patch
from fastapi.testclient import TestClient
from src.app import Foo, web_app
import pytest

client = TestClient(web_app)


@pytest.fixture()
def mock_foo_retorna_string_foo():
    with patch.object(target=Foo, attribute="retorna_string_foo", return_value="Prueba object") as mock:
        yield mock


def test_mock_string(mock_foo_retorna_string_foo):
    response = client.get("/api/v2")
    assert response.json() == mock_foo_retorna_string_foo.return_value
