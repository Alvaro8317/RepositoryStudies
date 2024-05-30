from unittest.mock import Mock
import json

mock = Mock()
print(mock)  # Indica el ID del mock
# Si existe un atributo, lo utiliza, de lo contrario, lo crea
# Vuelve a crear otro mock distinto al mock inicial, de manera recursiva
print(mock.prueba)  # Este método no existe, pero lo crea
print(mock.prueba.otra_prueba)  # Esto trata de simular el comportamiento de objetos reales
print(mock.prueba())
print(mock.prueba(a=1, b=2).sarasa())  # Por eso se llama lazy, si existe lo usa, si no, lo simula
print(json.dumps({"a": 1, "b": 2}))
json = Mock()
print(json)
print(json.dumps)
json.dumps.return_value = "prueba de mock"
print(json.dumps({"a": 1, "b": 2})) # Modifica la implementación original
