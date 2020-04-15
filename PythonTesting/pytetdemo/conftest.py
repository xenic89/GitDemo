import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executed first")
    yield
    print("I will be executed last")


@pytest.fixture()
def data_Load():
    print("user profile data is being created")
    return ["Dinesh", "Kannan", "dineshkannan.com"]


@pytest.fixture(params=[("chrome", "Dinesh"), ("Firefox", "IE"), ("Aishwarya", "Kannan")])
def crossBrowser(request):
    return request.param
