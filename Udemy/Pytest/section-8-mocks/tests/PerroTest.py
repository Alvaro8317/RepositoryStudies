from unittest.mock import patch

class Perro:
    def ladrar(self):
        return "woof"

perro = Perro()
print(perro.ladrar())
# Esto no es un monkey patching implicito, es un mock sin alterar el objeto original
with patch.object(target=Perro, attribute="ladrar") as mock_perro:
    mock_perro.return_value = "Esto es un ladrido en forma de mock"
    print(perro.ladrar())