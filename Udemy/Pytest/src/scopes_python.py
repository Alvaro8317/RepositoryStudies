a = 1
b = a + 2
c = b + a + 5


def prueba():
    # Scope a nivel de función
    # shadows name significa que existe una variable igual por fuera del scope
    global a
    a = 100
    print(a)
    b = 20
    print(b)


def prueba_2():
    # Este a solo existe aquí
    a = 20


class Clase:
    a = 1

    # A nivel de clase, este a se utiliza dentro de la clase porque es una propiedad de la clase
    def metodo(self):
        print(self.a)


prueba()
print(a)
print(b)
