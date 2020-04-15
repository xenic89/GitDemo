from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckOutPage


class HomePage():

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    chkbox = (By.ID, "exampleCheck1")
    dropDown =(By.ID, "exampleFormControlSelect1")
    Submit = (By.XPATH, "//input[@value='Submit']")
    SucMsg = (By.CLASS_NAME, "alert-success")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckOutPage(self.driver)
        return checkoutPage

    def enter_Name(self):
        return self.driver.find_element(*HomePage.name)

    def enter_Email(self):
        return self.driver.find_element(*HomePage.email)

    def check_box(self):
        return self.driver.find_element(*HomePage.chkbox)

    def drop_down(self):
        return self.driver.find_element(*HomePage.dropDown)

    def Submit_form(self):
        return self.driver.find_element(*HomePage.Submit)

    def succ_text(self):
        return self.driver.find_element(*HomePage.SucMsg).text


