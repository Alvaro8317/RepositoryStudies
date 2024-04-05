import pytest

@pytest.fixture
def fixture_name():
    return "Alvaro"

def test_prueba(fixture_name):
    assert fixture_name == "Alvaro"