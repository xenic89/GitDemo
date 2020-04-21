
import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="D:\\PyCharm Community Edition 2019.3.3\\chromedriver.exe")

    elif browser_name == "firefox":
        driver = webdriver.Chrome(executable_path="D:\\PyCharm Community Edition 2019.3.3\\geckodriver.exe")

    elif browser_name == "edge":
        driver = webdriver.Chrome(executable_path="D:\\PyCharm Community Edition 2019.3.3\\msedgedriver.exe")

    driver.get("http://automationpractice.com/index.php")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()
