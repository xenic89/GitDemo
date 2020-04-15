from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="D:\\PyCharm Community Edition 2019.3.3\\chromedriver.exe")


driver.get("https://rahulshettyacademy.com/angularpractice")

driver.find_element_by_css_selector("a[href*='shop']").click()
products = driver.find_elements_by_xpath("//div[@class='card h-100']")

for i in products:
    pname = i.find_element_by_xpath("div/h4/a").text
    if pname == "Blackberry":
        i.find_element_by_xpath("/div/button").click()

driver.find_element_by_css_selector("a[class*='nav-link btn']").click()
driver.find_element_by_css_selector("button[class*='btn-success']").click()
driver.find_element_by_css_selector("input[class*='filter-input']").send_keys("ind")
wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//a[text()='India']")))
driver.find_element_by_xpath("//a[text()='India']").click()

driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
driver.find_element_by_css_selector("input[type='submit']").click()
txt = driver.find_element_by_class_name("alert-success").text

assert "Success! Thank you!" in txt

driver.get_screenshot_as_file("screen.png")

print("This is the fourth change")
