from selenium import webdriver
from selenium.webdriver.support import wait
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="D:\\PyCharm Community Edition 2019.3.3\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

chekbox = driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(chekbox))

for i in chekbox:
    if i.get_attribute("value") == "option2":
        i.click()
        assert i.is_selected()

radio = driver.find_elements_by_name("radioButton")

radio[2].click()

assert driver.find_element_by_id("displayed-text").is_displayed()

driver.find_element_by_id("hide-textbox").click()

assert not driver.find_element_by_id("displayed-text").is_displayed()
