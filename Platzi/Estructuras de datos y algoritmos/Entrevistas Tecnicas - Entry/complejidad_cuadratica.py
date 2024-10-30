def complejidad_cuadratica(matriz) -> None:
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] != 0:
                print(matriz[i][j])


def test_complejidad_cuadratica(matriz_arg) -> None:
    print("Empezando ejecucion de: ", matriz_arg)
    complejidad_cuadratica(matriz_arg)


test_complejidad_cuadratica([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
test_complejidad_cuadratica([[1, 0, 1], [0, 1, 0], [2, 2, 2]])
