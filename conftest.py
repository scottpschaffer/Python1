import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

@pytest.fixture(scope="class")
def setup():
    print("I will be executed first")
    yield
    print("I will be executed last")

@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return {"name": "John Doe", "email": "john.doe@example.com"}

@pytest.fixture(params=[("Chrome", "Scott"), ("Firefox", "John"), ("IE", "Alice")])
def crossBrowser(request):
    return request.param

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="Chrome", help="Browser to run tests against"
    )

@pytest.fixture(scope="function")
def browserInstance(request):
    service_obj = Service("C:\\Users\\scott\\Python\\chromedriver.exe")
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "Chrome":
        driver = webdriver.Chrome(service=service_obj)
        driver.implicitly_wait(5)
    elif browser_name == "Firefox":
        driver = webdriver.Firefox(service=service_obj)
        driver.implicitly_wait(5)
    elif browser_name == "IE":
        driver = webdriver.Ie(service=service_obj)
        driver.implicitly_wait(5)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    
    yield driver
    driver.quit()