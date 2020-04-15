import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="D:\\PyCharm Community Edition 2019.3.3\\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

lst = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
lst1 = []
#print(lst)

driver.find_element_by_class_name("search-keyword").send_keys("ber")
time.sleep(3)
webe = driver.find_elements_by_xpath("//div[@class='products']/div/h4")

for i in webe:
    lst1.append(i.text)

print(lst1)
assert lst == lst1
