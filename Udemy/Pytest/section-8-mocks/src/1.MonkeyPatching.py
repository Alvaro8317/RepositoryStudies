class Perro:
    pass

# Monkey patching es modificar el comportamiento de un código en tiempo de ejecución
Perro.ladrar = lambda self: "woof woof"

perro1 = Perro()
print(perro1.ladrar())
