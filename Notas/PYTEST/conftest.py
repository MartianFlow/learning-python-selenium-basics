# Este archivo nos permite configurar un fixture general que podra ser usado por todos los test
import pytest


@pytest.fixture()
def setup():
    print("Me ejecuto de primeras: funcion setup")
    yield
    print("Me ejecuto de ultimas luego del yield")


@pytest.fixture(scope="class")
def setup_por_clase():
    print("Me ejecuto antes de los test de la clase")
    yield
    print("Me ejecuto despues de los test de la clase")


@pytest.fixture()
def data_test():
    print("Data requerida para la prueba")
    return ["nombre", "apellido", 30]


@pytest.fixture(params=[("Chrome", "name1", 20), ("Firefox", "name2", 30), "Edge"])
def data_params(request):
    return request.param
