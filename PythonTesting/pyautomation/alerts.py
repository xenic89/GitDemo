from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\PyCharm Community Edition 2019.3.3\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
actual = "Dinesh"
driver.find_element_by_css_selector("#name").send_keys("Dinesh")
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
txt = alert.text
assert actual in txt
alert.accept()

driver.find_element_by_css_selector("#confirmbtn").click()
alrt = driver.switch_to.alert
print(alrt.text)
alrt.dismiss()
