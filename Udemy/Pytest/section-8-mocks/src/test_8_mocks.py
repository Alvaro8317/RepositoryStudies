# patch es un helper que crea un mock a partir de unas definiciones
from unittest.mock import patch


class Perro:
    def ladrar(self):
        return "woof"


perro = Perro()
print(perro.ladrar())
