"""Cada pedazo tiene su respectiva complejidad"""


def complejidad_lineal(lista) -> tuple:
    """Complejidad de O(1) - Constante"""
    suma = 0
    multiplicacion = 1
    """ Complejidad de O(n) - Líneal """
    for numero in range(len(lista)):
        suma += numero
        print("suma:", suma, ", numero: ", numero)

    """ Complejidad de O(n) - Líneal """
    for numero in range(len(lista)):
        multiplicacion *= numero

    """Complejidad de O(1) - Constante"""
    return suma, multiplicacion


print(complejidad_lineal([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
