import pytest


@pytest.fixture(scope="class")
def setup():
    print("all you need is love")
    yield
    print("Test Finish ")


@pytest.fixture(params=["chrome ", "FireFox"])
def date(request):
    return request.param


@pytest.fixture()
def Datetype():
    return ["Gilad", "Rosnsewig"]
