import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# from selenium.webdriver.support.wait import expected

lst = []
lst1 = []
driver = webdriver.Chrome(executable_path="D:\\PyCharm Community Edition 2019.3.3\\chromedriver.exe")
#driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(3)

count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))

assert count == 3

buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
#//div[@class='product-action']/button/parent::div/parent::div/h4
for i in buttons:
    lst.append(i.find_element_by_xpath("parent::div/parent::div/h4").text)
    i.click()

print(lst)

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promoCode")))

vegg = driver.find_elements_by_css_selector("p.product-name")

for i in vegg:
    lst1.append(i.text)

print(lst1)
assert lst == lst1

totalamt = driver.find_element_by_css_selector("span.totAmt").text



driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()

wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promoInfo")))
print(driver.find_element_by_class_name("promoInfo").text)
discountedamt = driver.find_element_by_css_selector("span.discountAmt").text

print(totalamt)
print(discountedamt)

assert float(discountedamt) < float(totalamt)

values = driver.find_elements_by_xpath("//tr/td[5]/p")

sum = 0

for i in values:
    sum += int(i.text)

print(sum)

assert sum == int(totalamt)