# Se preserva el fixture dentro del mismo modulo, cada modulo es un archivo de python distinto
def test_module_1(fixture_module):
    print(fixture_module)


def test_module_2(fixture_module):
    print(fixture_module)


class TestModule:
    def test_module_from_class(self, fixture_module):
        print(fixture_module)

# Para ejecutar: pytest -k test_scope_modules -s
# -s es para que muestre los print
