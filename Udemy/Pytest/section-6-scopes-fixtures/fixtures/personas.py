import pytest

@pytest.fixture()
def fix_name():
    return "Alvaro"

@pytest.fixture()
def fix_lastname():
    return "Garzon"

@pytest.fixture()
def fix_dni():
    return 123