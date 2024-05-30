# Método para saber si un método fue ejecutado o no
import json
from unittest.mock import Mock

print(dir(json))
print(json.dumps({"a": 1}))
json = Mock()
print(json.dumps)  # Se crea el método, se mockea
json.dumps()
print(json.dumps.assert_called())  # Da error si nunca se ha invocado, si se ejecutó, da None
print(json.dumps.assert_called_once())  # Da error si se ejecutó una cantidad de veces distinta a 1
# assert_called_once retorna cuantas veces se invocó en caso de excepción y sus parámetros
print(dir(json))
json.dumps()
print(json.dumps.call_count)  # Cantidad de veces que fue invocado el método
# Esto es útil para saber si un mock se ha ejecutado o no
# Se puede ver este tipo de asserts con testing en frontend
print(json.dumps("manzana"))
json.dumps.assert_called_with("manzana")  # Valida si un llamado con un parámetro se ha ejecutado
