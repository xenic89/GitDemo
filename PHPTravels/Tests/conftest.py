
import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path="D:\\PyCharm Community Edition 2019.3.3\\chromedriver.exe")
    driver.get("http://automationpractice.com/index.php")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
