import pytest
from src import sumar

""" Pytest detecta este patrón """
""" Estos no son los test, son los modulos de los test """
""" Para que pytest detecte el test, debe de empezar con la palabra test """

@pytest.mark.prueba
def test_no_falla():
    assert sumar(1, 1) == 2


def test_falla():  # Explota el test
    assert sumar(1, 1) == 20


def helado_prueba():
    pass
