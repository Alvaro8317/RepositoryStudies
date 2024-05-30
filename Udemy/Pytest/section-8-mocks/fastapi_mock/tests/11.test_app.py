import pytest
from unittest.mock import Mock
import requests
from requests import Request, Timeout

requests = Mock()


def test_connection():
    requests.get.side_effect = Timeout
    with pytest.raises(Timeout):
        response: Request = requests.get("http://www.google.com", timeout=5)
        print(response.text)
