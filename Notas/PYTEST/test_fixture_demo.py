import pytest

#Esta funcion se ejecuta antes de cualquier otra
@pytest.fixture()
def setup():
    print("Me ejecuto de primeras: funcion setup")
    yield
    print("Me ejecuto de ultimas luego del yield")


#tenemos la opcion de ejecutar la funcion fixture en otras funciones, para esto lo hacemos pasandola como argumento de dichas funciones
def test_login(setup):
    print("Se ejecuta despues del setup, utiliza el setup como argumento")


def test_bandeja():
    print("No utilizo el setup")