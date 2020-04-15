import pytest

@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDeno(self):
        print("I will excue steps in fixtureDemo methond")

    def test_fixtureDeno1(self):
        print("I will excue steps in fixtureDemo1 methond")

    def test_fixtureDeno2(self):
        print("I will excue steps in fixtureDemo2 methond")

    def test_fixtureDeno3(self):
        print("I will excue steps in fixtureDemo3 methond")