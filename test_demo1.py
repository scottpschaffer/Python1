# Any pytest file should start with test_ or end with _test.py
# pytest method names should start with test_
import pytest

@pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello, World!")
    assert 1 + 1 == 2

def test_secondProgram():
    print("Goodbye, World!")
    assert 1 + 1 == 2

def test_crossBrowser(crossBrowser):
    print(crossBrowser)
    print(crossBrowser[0])
    print(crossBrowser[1])