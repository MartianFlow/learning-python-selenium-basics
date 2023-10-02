import pytest


@pytest.mark.usefixtures("data_test")
class TestFixtureData:
    def test_uso_data_login(self, data_test):
        print(data_test[0])
        print(data_test[2])
