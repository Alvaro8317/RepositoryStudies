from unittest.mock import Mock
import json

# Cuando no encuentra un atributo o método de un mock, si no tiene una definición, retorna otro mock
mock = Mock()
print(mock)  # <Mock id='2034824739344'>

# Atributo perezoso, el mock no tiene este atributo, pero aún así existe. Este es un nuevo mock
# Crea un mock en parte a mock, es decir, mock.test != mock
print(mock.test)  # <Mock name='mock.test' id='2401180843856'>

print(mock.metodo_que_no_existe())  # <Mock name='mock.metodo_que_no_existe()' id='1601219664912'>, como no existe

print(json.dumps({"a": 1, "b": 2}))
json = Mock()
json.dumps.return_value = "Prueba de mock"
print(json.dumps({"a": 1, "b": 2}))
