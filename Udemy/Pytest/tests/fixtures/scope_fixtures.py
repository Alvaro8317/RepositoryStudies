import pytest
import random
import sqlite3

c1 = 0
c2 = 0
c3 = 0
c4 = 0
counter_module = 0


# por defecto el scope es de function, sin parentesis aplica por defecto
@pytest.fixture(scope="function")
def fixture_function():
    # Uso para una sola vez, como lectura de un archivo o hace operaciones ligeras, también utilizable cuando va a
    # retornar un dato distinto
    global c1
    c1 += 1
    return f"fixture con el scope en function - repeticiones: {c1}"


@pytest.fixture(scope="class")
def fixture_class():
    global c2
    c2 += 1
    return f"fixture con el scope en class - repeticiones: {c2}"


@pytest.fixture(scope="module")
def fixture_module():
    global counter_module
    counter_module += 1
    return f"Fixture con el scope en module - repeticiones {counter_module}"

@pytest.fixture(scope="package")
def fixture_pck():
    global c3
    c3 += 1
    return f"fixture con el scope en package - repeticiones: {c3}"

# Fixture que solo se ejecutará una sola vez, ideal para operaciones costosas como leer archivos pesados
# conexiones a bases de datos, etc.
# Así se ejecute desde diferentes modulos, solo se ejecutará una vez
@pytest.fixture(scope="session")
def fixture_session():
    global c4
    c4 += 1
    return f"fixture con el scope en sesiones - repeticiones: {c4}"



# ------------------------------------------------- Functions -------------------------------------------------
# Útil si solo se leerá el archivo por cada ejecución
@pytest.fixture(scope="function")
def read_file():
    with open("archivo.txt", "r") as file:
        text = file.read()
    return text


# Si retorna siempre lo mismo, podría usarse a nivel de sesión o clase
@pytest.fixture()
def light_operation():
    lista: list = [1, 2, 3, 4]
    return sum(list)


# Ideal como function para que siempre retorne un numero distinto, si se requeriría modificar para que solo
# se ejecute una vez, lo ideal es cambiarle el scope
@pytest.fixture()
def random_number():
    return random.randint(1, 200)


# ------------------------------------------------- CLASS -------------------------------------------------
# Se va a ejecutar cada vez que lo invoque una clase y se reutilizará a nivel de clase
# Útil para dar una configuración a una clase especifica
@pytest.fixture(scope="class")
def random_number_class():
    return random.randint(1, 200)


# Aplicando una configuración a nivel de clase con request
@pytest.fixture(scope="class")
def set_attributes_of_class(request):
    # Request es una fixture tipo funcion nativa de pytest que hace referencia al que la llama en sí
    request.cls.a = 1
    request.cls.b = 2


@pytest.fixture(scope="class")
def set_attributes_of_database(request):
    db = sqlite3.connect("test.db")
    request.cls.db = db
    request.cls.cursor = db.cursor()
    yield
    request.cls.cursor.close()
    request.cls.db.close()
