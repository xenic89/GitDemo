from selenium.webdriver.common.by import By

class confirmPage:

    confirm = (By.CSS_SELECTOR, "button[class*='btn-success'")
    country = (By.CSS_SELECTOR, "input[class*='filter-input']")
    appear_country = (By.XPATH, "//a[text()='India']")
    checkB_ox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchase_button = (By.CSS_SELECTOR, "input[type='submit']")
    Success_text = (By.CLASS_NAME, "alert-success")
    def __init__(self, driver):
        self.driver = driver

    def confirmPage(self):
        return self.driver.find_element(*confirmPage.confirm)

    def coun_try(self):
        return self.driver.find_element(*confirmPage.country)

    def country_appear(self):
        return self.driver.find_element(*confirmPage.appear_country)

    def check_box(self):
        return self.driver.find_element(*confirmPage.checkB_ox)

    def purch_Button(self):
        return self.driver.find_element(*confirmPage.purchase_button)

    def Suc_text(self):
        return self.driver.find_element(*confirmPage.Success_text).text