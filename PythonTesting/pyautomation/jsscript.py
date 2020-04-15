from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\PyCharm Community Edition 2019.3.3\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_name("name").send_keys("hello")

print(driver.find_element_by_name("name").text)


print(driver.find_element_by_name("name").get_attribute("value"))

print(driver.execute_script('return document.getElementsByName("name")[0].value'))


shopB = driver.find_element_by_css_selector("a[href*='shop']")
driver.execute_script("arguments[0].click();", shopB)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#driver.close()

print('This is the fifth change')