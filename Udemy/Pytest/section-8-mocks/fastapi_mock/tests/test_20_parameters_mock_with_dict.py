
from unittest.mock import patch
from fastapi.testclient import TestClient
from src.app import Foo, web_app
import pytest

client = TestClient(web_app)



@pytest.fixture()
def mock_bar(request):
    with patch.object(target=Foo, attribute="retorna_is_a_number",
                      return_value=request.param.get("return_value")) as mock:
        # Se setea un atributo al mock como expected_response
        mock.expected_response = request.param.get("expected_response")
        yield mock


@pytest.mark.parametrize("mock_bar",
                         [
                             {"return_value": "123", "expected_response": "is a number"},
                             {"return_value": "abc", "expected_response": "is not a number"},
                         ], indirect=["mock_bar"])
def test_mock_string(mock_bar):
    response = client.get("/api/v3")
    assert response.json() == mock_bar.expected_response
