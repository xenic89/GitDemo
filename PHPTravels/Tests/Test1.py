from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="D:\\PyCharm Community Edition 2019.3.3\\chromedriver.exe")

driver.get("http://automationpractice.com/index.php")

driver.find_element_by_css_selector("a[title='Women']").click()
url = driver.current_url
assert "http://automationpractice.com/index.php?id_category=3&controller=category" in url
driver.back()

driver.find_element_by_xpath("//div/ul/li/a[text()='Dresses']").click()
url2 = driver.current_url
assert "http://automationpractice.com/index.php?id_category=8&controller=category" in url2
driver.back()

driver.find_element_by_xpath("//div/ul/li/a[text()='T-shirts']").click()
url3 = driver.current_url
assert "http://automationpractice.com/index.php?id_category=5&controller=category" in url3

driver.close()