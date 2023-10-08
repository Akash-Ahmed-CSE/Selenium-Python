import pytest
@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "Hellow"
    assert msg == "Hi", "Test falied because condition not match "


def test_secindProgram():
    a = 4
    b = 6
    assert a+2 == 6, "Addition not match"


@pytest.fixture()
def setup():
    print(" I will be executing firsr")

def test_fixtureDemo(setup):
    print(" I will execute steps in fixturedemo method")