from selenium.webdriver.common.by import By


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    dresscheckout = (By.XPATH, "//a[text()='Faded Short Sleeve T-shirts']")
    pricecheckout = (By.XPATH, "//td[@class='cart_unit']/span/span")
    quantitycheckout = (By.CSS_SELECTOR, "td input[type='hidden']")

    def dress_checkout(self):
        return self.driver.find_element(*CheckOutPage.dresscheckout)

    def price_checkout(self):
        return self.driver.find_element(*CheckOutPage.pricecheckout)

    def quantity_checkout(self):
        return self.driver.execute_script(*CheckOutPage.quantitycheckout)