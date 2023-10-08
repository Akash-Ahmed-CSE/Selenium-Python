import pytest
@pytest.fixture()
def setup():
    print(" I will be executing firsr")
    yield
    print(" I will be executed last")

def dataLoan():
    print("user profile data is being created")
    return ["Akash","Ahmed","akash@gmail.com"]