from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="D:\\PyCharm Community Edition 2019.3.3\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")

#driver.find_element_by_name("name").send_keys("Dinesh Kannan")
driver.find_element_by_css_selector("input[name='name']").send_keys("Dinesh Kannan")
driver.find_element_by_name("email").send_keys("din@abc.com")
driver.find_element_by_id("exampleCheck1").click()

dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
driver.find_element_by_xpath("//input[@value='Submit']").click()

message = driver.find_element_by_class_name("alert-success").text
assert "success" in message