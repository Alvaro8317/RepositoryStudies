import pytest
from random import randint
@pytest.fixture()
def generate_number():
    return randint(0, 100)