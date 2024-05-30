class Gato:
    pass


# Monkey patching, se modifica el comportamiento en tiempo real, utilizado en mocks
Gato.maullar = lambda self: "Miau"
gato_1 = Gato()
print(gato_1.maullar())

# patch es un helper que crea un mock a partir de unas definiciones
from unittest.mock import patch


class Perro:
    def ladrar(self):
        return "woof"


perro = Perro()
print(perro.ladrar())
# object para objetivos como objetos
# Así crea un objeto duumie que imitará Perro y se llamará mock
# With es un context manager
# Crea un objeto a partir de otro modificando su implementación, sin modificar la original
with patch.object(target=Perro, attribute="ladrar") as mock_perro:
    mock_perro.return_value = "Ladrido en forma de mock"
    print(perro.ladrar())
