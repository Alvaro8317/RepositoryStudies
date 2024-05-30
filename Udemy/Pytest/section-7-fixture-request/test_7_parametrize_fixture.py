import pytest


@pytest.fixture()
def fxt_parametrize(request):
    print(request.param)
    return request


# Aquí no toma el fixture porque primero va el nombre del parámetro del test
# luego los valores
@pytest.mark.parametrize(
    "fxt_parametrize",
    [
        555,
        "string",
        (1, 2, 3, 4),
        {"clave": "valor"}
    ]
)
def test_fxt_no_toma_fixture(fxt_parametrize):
    assert True


# Para este caso, los parámetros se le pasarían a la fixture
@pytest.mark.parametrize(
    "fxt_parametrize",
    [
        555,
        "string",
        (1, 2, 3, 4),
        {"clave": "valor"}
    ],
    indirect=True  # Por defecto es False
)
def test_fxt_toma_fixture(fxt_parametrize):
    assert True


# También funcional, con diferencia que se le especifica la fixture a pasar los parametros
# En pytest está la parametrización explicita o implicita con las fixture
# En este ejemplo es similar a la parametrización implicita aunque no muy usada
@pytest.mark.parametrize(
    "fxt_parametrize",
    [
        555,
        "string",
        (1, 2, 3, 4),
        {"clave": "valor"}
    ],
    indirect=["fxt_parametrize"]
)
def test_fxt_toma_fixture(fxt_parametrize):
    assert True


class Usuario:
    def __init__(self, nombre: str, rol: str):
        self.nombre = nombre
        self.rol = rol


def ingresar_boveda(usuario: Usuario):
    if usuario.rol in ["admin", "cliente"]:
        return True
    return False


@pytest.fixture()
def usuario(request):
    return Usuario(nombre=request.param["nombre"], rol=request.param["rol"])


@pytest.mark.parametrize(
    "usuario",
    [
        {"nombre": "Alvaro", "rol": "admin", "expected_result": True},
        {"nombre": "Eduardo", "rol": "cliente", "expected_result": True},
        {"nombre": "Mylou", "rol": "comprador", "expected_result": False},
    ],
    indirect=True)
def test_acceso_boveda(request, usuario):
    assert ingresar_boveda(usuario=usuario) is request.node.callspec.params["usuario"]["expected_result"]