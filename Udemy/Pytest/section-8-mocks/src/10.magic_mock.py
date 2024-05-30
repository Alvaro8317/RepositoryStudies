from unittest.mock import Mock, MagicMock

m1 = Mock()
# m1[3] = "Test" # No soportado por Mock()
m2 = MagicMock()
m2[3] = "Test"
print(m2)
print(m2[3])  # Genera un mock distinto
m2.__setitem__.assert_called_with(3, "Test")
m2.__setitem__.assert_called_with(3, "Test2")
# Magic Mock es el mismo Mock pero con más funcionalidades. Un patch lo que genera es un Magic Mock
