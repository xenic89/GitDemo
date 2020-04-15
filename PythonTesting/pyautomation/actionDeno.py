import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="D:\\PyCharm Community Edition 2019.3.3\\chromedriver.exe")

#driver.get("https://www.wvi.org/")

#action = ActionChains(driver)

#action.move_to_element(driver.find_element_by_class_name("our-work")).perform()


#action.move_to_element(driver.find_element_by_link_text("EDUCATION")).click().perform()

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
action = ActionChains(driver)
#action.context_click(driver.find_element_by_id("double-click")).click().perform()
action.double_click(driver.find_element_by_id("double-click")).click().perform()

alert = driver.switch_to.alert
print(alert.text)
assert "You double clicked me!!!, You got to be kidding me" == alert.text
alert.accept()
