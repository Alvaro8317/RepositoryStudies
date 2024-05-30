# Es la combinación de los dos anteriores
import json
from unittest.mock import Mock

json.dumps({"prueba": "texto"})
json = Mock()

# json.dumps("Pera")
json.dumps("Pera")
json.dumps.assert_called_once_with("Pera")
