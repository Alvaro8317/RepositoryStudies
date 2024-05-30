from unittest.mock import Mock

mock = Mock()


def prueba():
    return "Hello world"


mock.side_effect = prueba
# mock.side_effect = Exception

print(mock())
