from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="D:\\PyCharm Community Edition 2019.3.3\\chromedriver.exe")
driver.get("https://makemytrip.com")

driver.find_element_by_id("fromCity").click()
driver.find_element_by_css_selector("input[placeholder='From']").send_keys("del")
cities = driver.find_elements_by_css_selector("p[class*='blackText']")
print(len(cities))
for i in cities:
    if i.text == "Deline, Canada":
        i.click()

driver.find_element_by_xpath("//p[text()='Mumbai, India']").click()

print("There has been a change in the code")
print("There will be a change in the code")