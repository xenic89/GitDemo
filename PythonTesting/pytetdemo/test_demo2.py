import pytest

@pytest.mark.smoke
@pytest.mark.skip
def test_thirdprogram():
    msg = "Hello"
    assert msg == "Hi", "Test failed because strings do not match"


def test_fourthCreditprogram():
    a = 4
    b = 6
    assert a+2 == b, "Addition do not match"