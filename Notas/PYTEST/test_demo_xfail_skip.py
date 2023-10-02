# los archivos que se usaran con pytest se deben nombrar siempre con el estandar test_
# igual con las funciones, deben empezar con test_nombre_funcion
import pytest


@pytest.mark.xfail
def test_primer_test():
    print("Hola Tester")


@pytest.mark.skip
def test_login():
    print("prueba Login 1")
