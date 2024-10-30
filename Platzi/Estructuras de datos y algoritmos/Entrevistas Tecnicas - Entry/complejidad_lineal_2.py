"""Cada pedazo tiene su respectiva complejidad"""


def complejidad_lineal_2(lista) -> tuple:
    calculo = 0
    """Complejidad lineal"""
    for i in range(len(lista)):
        """Complejidad constante"""
        for j in range(1, 5):
            calculo += i * j
    """O(5) + O(n) = O(n)"""
    return calculo


print(complejidad_lineal_2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
