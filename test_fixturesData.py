import pytest

@pytest.mark.usefixtures("dataLoad")
class TestExamples2:
    def test_example1(self, dataLoad):
        print(dataLoad)
