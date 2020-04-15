from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\PyCharm Community Edition 2019.3.3\\chromedriver.exe")
#iframe, frameset,frame
driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
#frame id, name or index value
driver.find_element_by_css_selector("#tinymce").clear()
driver.find_element_by_css_selector("#tinymce").send_keys("I am able to enter the text")
driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h3").text)