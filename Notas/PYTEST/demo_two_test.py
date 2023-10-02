import pytest


@pytest.mark.smoke
def test_assert_message(setup):
    text = "Hello"
    assert text == "Hi", "El texto es diferente"


def test_login():
    print("prueba Login 2")