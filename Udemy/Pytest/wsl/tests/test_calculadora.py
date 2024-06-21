import pytest
from src import Calculadora


@pytest.mark.calculadora
class TestCalculadora:
    def test_sumar(self):
        calculator = Calculadora()
        result = calculator.sumar(5, 5)
        assert result == 10

    def test_restar(self):
        result = Calculadora.restar(10, 5)
        assert result == 5

    def test_multiplicar(self):
        result = Calculadora.multiplicar(10, 10)
        assert result == 100

    def test_dividir(self):
        result = Calculadora.dividir(10, 5)
        assert result == 2

    """ Diferente a """

    def test_falla_sumar(self):
        calculator = Calculadora()
        result = calculator.sumar(5, 50)
        assert result != 10

    """ Parametrización """

    @pytest.mark.parametrize(
        "num1, num2, expected", [(1, 5, 6), (10, 10, 20), (100, 100, 200)]
    )
    def test_sumar_parametrize(self, num1, num2, expected):
        result = Calculadora().sumar(num1, num2)
        assert result == expected

    @pytest.mark.parametrize(
        "num1, num2, expected", [(1, 5, 5), (10, 10, 100), (100, 100, 10000)]
    )
    def test_multiplicar_parametrize(self, num1, num2, expected):
        result = Calculadora.multiplicar(num1, num2)
        assert result == expected