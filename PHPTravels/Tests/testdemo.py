import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="D:\\PyCharm Community Edition 2019.3.3\\chromedriver.exe")

driver.get("http://automationpractice.com/index.php")
driver.maximize_window()

#login
driver.find_element_by_css_selector("div a[class='login']").click()
driver.find_element_by_id("email").send_keys("din@abc.com")
driver.find_element_by_id("passwd").send_keys("123456")
driver.find_element_by_id("SubmitLogin").click()
driver.find_element_by_xpath("//div/a/img[@alt='My Store']").click()

driver.find_element_by_xpath("//*[contains(@class, 'footer')]/h4/a/parent::h4/parent::section/div/ul/li/a[@title='Sign out']")
assert driver.current_url == "http://automationpractice.com/index.php?controller=authentication&back=my-account"
driver.close()