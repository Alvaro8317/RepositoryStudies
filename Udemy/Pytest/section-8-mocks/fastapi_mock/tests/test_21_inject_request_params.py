from functools import wraps
from unittest.mock import patch
from fastapi.testclient import TestClient
from src.app import Foo, web_app
import pytest

client = TestClient(web_app)


def inject_request_param(fixture):
    @wraps(fixture)
    def wrapper(request, *args, **kwargs):
        if not hasattr(request, "param"):
            setattr(request, "param", {})
        yield from fixture(request=request, *args, **kwargs)

    return wrapper


@pytest.fixture()
@inject_request_param
def mock_bar(request):
    with patch.object(target=Foo, attribute="retorna_is_a_number") as mock:
        mock.return_value = request.param.get("return_value", "111")
        mock.expected_response = request.param.get("expected_response", "is a number")
        yield mock


def test_mock_string(mock_bar):
    response = client.get("/api/v3")
    assert response.json() == mock_bar.expected_response
