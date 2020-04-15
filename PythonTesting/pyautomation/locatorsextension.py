from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\PyCharm Community Edition 2019.3.3\\chromedriver.exe")
driver.get("https://login.salesforce.com/")

driver.find_element_by_css_selector("#username").send_keys("Dinesh")
driver.find_element_by_css_selector(".password").send_keys("Kannan")
driver.find_element_by_css_selector(".password").clear()

driver.find_element_by_link_text("Forgot Your Password?").click()
driver.find_element_by_xpath("//a[text()='Cancel']").click()
print(driver.find_element_by_xpath("//form[@id='login_form']/div[1]/label").text)
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(3)").text)