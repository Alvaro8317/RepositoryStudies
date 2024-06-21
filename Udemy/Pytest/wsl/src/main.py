def sumar(a: int, b: int) -> int:
    return a + b


class Calculadora:
    def sumar(self, a: int, b: int) -> int:
        return a + b

    """ Con métodos de clase se pueden acceder a todas las propiedades de la clase sin crear una instancia """

    @classmethod
    def restar(cls, a: int, b: int) -> int:
        return a - b

    """ Con métodos estáticos es una función encapsulada a una clase, a diferencia de classmethod es que no puede acceder a las propiedades o atributos de la clase """
    @staticmethod
    def multiplicar(a: int, b: int) -> int:
        return a * b

    @staticmethod
    def dividir(a: int, b: int) -> float:
        return a / b
