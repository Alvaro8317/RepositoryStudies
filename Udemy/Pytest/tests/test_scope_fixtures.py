# Tests de introducción
import pytest


def test_scope_function(fixture_function):
    print(fixture_function)


def test_scope_function_2(fixture_function):
    print(fixture_function)


def test_scope_session(fixture_session):
    print(fixture_session)


def test_scope_session_2(fixture_session):
    print(fixture_session)


# Test de funciones
def test_scope_function_random(random_number):
    print(random_number)


def test_scope_function_random_2(random_number):
    print(random_number)


# Test de clases
class TestClassScope:

    def test_scope_class_random_1(self, random_number_class):
        print(random_number_class)

    def test_scope_class_random_2(self, random_number_class):
        print(random_number_class)


class TestClassScope2:

    def test_scope_class_random_1(self, random_number_class):
        print(random_number_class)

    def test_scope_class_random_2(self, random_number_class):
        print(random_number_class)


@pytest.mark.usefixtures("set_attributes_of_class")
class TestClassScopeAttributes:
    def test_print_a(self):
        print(f"Atributo 'a' tiene un valor de: {self.a}")

    def test_print_b(self):
        print(f"Atributo 'b' tiene un valor de: {self.b}")


# Se le inyectan los valores o atributos de clase reutilizando código
@pytest.mark.usefixtures("set_attributes_of_class", "set_attributes_of_database")
class TestClassScopeAttributes2:
    def test_print_a(self):
        print(f"Atributo 'a' PRUEBA 2 tiene un valor de: {self.a}")

    def test_print_b(self):
        print(f"Atributo 'b' PRUEBA 2 tiene un valor de: {self.b}")

    def test_database(self):
        self.cursor.execute("CREATE TABLE PERSONAS(ID INT, NAME VARCHAR);")
        self.cursor.execute("INSERT INTO PERSONAS (ID, NAME) VALUES (01, 'Alvaro')")
        print(self.cursor.execute("SELECT * FROM PERSONAS;").fetchall())
        self.cursor.execute("DROP TABLE PERSONAS;")
