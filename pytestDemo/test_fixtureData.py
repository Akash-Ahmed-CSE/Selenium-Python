import pytest
@pytest.mark.usefixtures("dataLoan")
class TestExample2:
    def test_editProfile(self,dataLoan):
        print(dataLoan[0])