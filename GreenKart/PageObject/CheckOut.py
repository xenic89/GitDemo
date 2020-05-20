from selenium.webdriver.common.by import By


class CheckOut:

    def __init__(self, driver):
        self.driver = driver

    agreebtn = (By.CLASS_NAME, "chkAgree")
    proceedbtn = (By.CSS_SELECTOR, "div button")

    def agree_btn(self):
        return self.driver.find_element(*CheckOut.agreebtn)

    def pro_btn(self):
        return self.driver.find_element(*CheckOut.proceedbtn)