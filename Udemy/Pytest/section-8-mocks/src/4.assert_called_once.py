import json
from unittest.mock import Mock

json.dumps({"prueba": "texto"})
json = Mock()

# Da error si no se ha invocado o se invocó más de una vez. Los parámetros no afectan
json.dumps()
json.dumps.assert_called_once()
json.dumps("test")
json.dumps.assert_called_once()
