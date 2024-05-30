from unittest.mock import patch
from fastapi.testclient import TestClient
from src.app import Foo, web_app
import pytest

client = TestClient(web_app)


@pytest.fixture()
def mock_bar(request):
    with patch.object(target=Foo, attribute="retorna_is_a_number", return_value=request.param) as mock:
        yield mock


@pytest.mark.parametrize("mock_bar, expected_response",
                         [
                             ("123", "is a number"),
                             ("abc", "is not a number")
                         ], indirect=["mock_bar"])
def test_mock_string(mock_bar, expected_response):
    response = client.get("/api/v3")
    assert response.json() == expected_response
