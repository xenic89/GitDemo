import time

from selenium import webdriver
from selenium.webdriver.support import wait
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="D:\\PyCharm Community Edition 2019.3.3\\chromedriver.exe")
driver.get("https://www.makemytrip.com/")

driver.find_element_by_id("fromCity").click()
driver.find_element_by_xpath("//input[@placeholder='From']").send_keys("del")

cities = driver.find_elements_by_css_selector("p[class*='blackText']")
time.sleep(2)
print(len(cities))
for city in cities:
    if city.text == 'Del Rio, United States':
        city.click()
        break
time.sleep(2)

<<<<<<< HEAD
driver.find_elements_by_css_selector("//p[text()='Pune, India']").click()


driver.find_elements_by_css_selector("//p[text()='Pune, India']").click()

def dinsh(self):
    print("Dinesh Kannan")

def kannan(self):
    print("Janaranjani Mohan")
    print("C S Kannan")
    
def Uma(self):
    print("Aishwarya Kannan")