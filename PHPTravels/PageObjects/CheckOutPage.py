from selenium.webdriver.common.by import By


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    dresscheckout = (By.XPATH, "//a[text()='Faded Short Sleeve T-shirts']")
    pricecheckout = (By.XPATH, "//td[@class='cart_unit']/span/span")

    def dress_checkout(self):
        return self.driver.find_element(*CheckOutPage.dresscheckout)

    def price_checkout(self):
        return self.driver.find_element(*CheckOutPage.pricecheckout)