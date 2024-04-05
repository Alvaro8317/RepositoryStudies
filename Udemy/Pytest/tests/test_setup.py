import pytest


@pytest.fixture()
def fix_database():
    print("ARRANGE")
    yield  # Tiene la capacidad de memorizar en qué estado está
    print("CLEAN UP")


def test_prueba(fix_database):
    print("Ejecutando")
    assert True
