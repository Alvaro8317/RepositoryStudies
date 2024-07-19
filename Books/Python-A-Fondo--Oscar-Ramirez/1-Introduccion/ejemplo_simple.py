import math


def hola_mundo():
    print("Hola mundo")


def calcular_raiz_cuadrada(num):
    return math.sqrt(num)


def main_function(long):
    hola_mundo()
    print([x * 2 for x in range(long)])
    while True:
        num = float(input("Ingrese un numero: "))
        result = calcular_raiz_cuadrada(num)
        print(f"La raiz cuadrada de {num} es {result}")


if __name__ == '__main__':
    main_function(5)
