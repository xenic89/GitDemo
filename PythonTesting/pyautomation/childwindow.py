from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\PyCharm Community Edition 2019.3.3\\chromedriver.exe")

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element_by_link_text("Click Here").click()
child1 = driver.window_handles[1]
driver.switch_to.window(child1)
print(driver.find_element_by_xpath("//h3").text)
driver.close()
parent = driver.window_handles[0]
driver.switch_to.window(parent)
print(driver.find_elements_by_xpath("//h3").text)
assert "Opening a new window" == driver.find_elements_by_xpath("//h3[@xpath='1']")

