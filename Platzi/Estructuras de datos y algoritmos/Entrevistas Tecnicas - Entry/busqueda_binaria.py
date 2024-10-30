def busqueda_binaria(lista, objetivo):
    """Complejida constante"""
    apuntador_izquierdo = 0
    apuntador_derecho = len(lista) - 1
    while apuntador_izquierdo <= apuntador_derecho:
        """ Complejidad logarítmica"""
        punto_medio = (apuntador_izquierdo + apuntador_derecho) // 2
        if lista[punto_medio] == objetivo:
            return punto_medio
        elif lista[punto_medio] < objetivo:
            apuntador_izquierdo = punto_medio + 1
        else:
            apuntador_derecho = punto_medio - 1
    return "Lista no ordenada"


print(busqueda_binaria([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
print(busqueda_binaria([1, 6, 7, 8, 9, 2, 3, 4, 5, 10], 11))
