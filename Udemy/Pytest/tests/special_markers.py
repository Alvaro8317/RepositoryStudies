import pytest
import sys


def verify_envs():
    return False


# Este test no se ejecutará, se salta, útil cuando una API no sirve o cosas similares
@pytest.mark.skip("Prueba que no se ejecutará")
def test_que_se_salta():
    assert False


def test_que_se_salta_explicitamente():
    if not verify_envs():
        pytest.skip("Las variables de entorno no se pudieron verificar")


def test_que_no_se_salta():
    assert True


# Se salta el test si el primer parametro es True
@pytest.mark.skipif(verify_envs() is False, reason="Test skipeado con skipif")
def test_que_se_salta_con_skipif():
    assert False


# Skip s cuando se espera que los test pasen solamente
@pytest.mark.skipif(sys.platform != "win32", reason="Test skipeado porque solo funciona en windows")
def test_que_no_se_salta_si_esta_en_windows():
    assert True


# Xfail es cuando se espera que un test falle, como una feature no implementada, un bug no arreglado aún
@pytest.mark.xfail
def test_xfail_true():
    print("\nSi el assert es false, se skipea, si es true, se ejecuta normalmente")
    assert True


@pytest.mark.xfail
def test_xfail_false():
    print("\nSi el assert es false, se skipea, si es true, se ejecuta normalmente")
    assert False


# Usefixtures

@pytest.fixture
def fxt_test():
    print("\nSoy una fxt, me ejecuto cada vez que me invocan")


@pytest.fixture
def fxt_test_2():
    print("\nSoy una fxt2, me ejecuto cada vez que me invocan")


@pytest.mark.usefixtures("fxt_test", "fxt_test_2")
class TestPruebaFixtures:
    def test_1(self):
        pass

    def test_2(self):
        pass

    def test_3(self):
        pass

    def test_4(self):
        pass

    def test_5(self):
        pass
