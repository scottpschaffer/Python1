import pytest

@pytest.mark.smoke
@pytest.mark.skip(reason="Skipping this test for now")
def test_firstProgram():
    print("Hello, World!")
    assert 4 + 2 == 6

@pytest.mark.xfail(reason="Expected to fail")
def test_secondProgram():
    print("Goodbye, World!")
    assert 1 + 1 == 3, "Math is broken!"

@pytest.mark.usefixtures("setup")
class TestDemo:
    def test_fixtureDemo1(self):
        print("Running test_fixtureDemo1")

    def test_fixtureDemo2(self):
        print("Running test_fixtureDemo2")