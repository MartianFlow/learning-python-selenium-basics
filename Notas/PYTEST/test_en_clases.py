import pytest


@pytest.mark.usefixtures("setup_por_clase")
class TestExample:
    def test_uno(self):
        print("imprime uno")

    def test_dos(self):
        print("imprime dos")