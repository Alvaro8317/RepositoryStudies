import json
from unittest.mock import Mock

json.dumps({"a": 1})
json: Mock = Mock()
json.dumps
json.dumps()
json.dumps.assert_called()  # Valida que el mock haya sido llamado

print(dir(json))

print(json.dumps.call_count)
json.dumps()
print(json.dumps.call_count)
