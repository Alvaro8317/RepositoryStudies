import json
from unittest.mock import Mock

json.dumps({"prueba": "texto"})
json = Mock()

# Da error si no se ha invocado un método con un parámetro en especifico o si no se ha llamado
json.dumps("Pera")
json.dumps.assert_called_with("Pera")
json.dumps.assert_called_with("Manzana")
