# pytest file should always start with test_ or end with _test
# any pytest method shouldstart withtest
import pytest

@pytest.mark.smoke
def test_firstCreditProgram():
    print("hello")


def test_secdprogram():
    print("Good Morning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])