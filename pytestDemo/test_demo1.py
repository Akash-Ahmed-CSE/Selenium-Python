# Any pytest file should start with test_ or end with _test

#Test mothod name start with test
#Any code shoul dbe wrapped in method only


import pytest
@pytest.mark.smoke
def test_firstProgram():
    print("Hello")



@pytest.mark.xfail
def test_fistProgram2():
    print("Good Morning")