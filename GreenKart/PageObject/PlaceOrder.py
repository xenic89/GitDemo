from selenium.webdriver.common.by import By


class PlaceOrder:

    def __init__(self, driver):
        self.driver = driver

    promocodee = (By.CLASS_NAME, "promoCode")
    promobtn = (By.CLASS_NAME, "promoBtn")
    promoinfo = (By.CLASS_NAME, "promoInfo")
    placorder = (By.XPATH, "//button[text()='Place Order']")

    def promo_code(self):
        return self.driver.find_element(*PlaceOrder.promocodee)

    def promo_btn(self):
        return self.driver.find_element(*PlaceOrder.promobtn)

    def promo_info(self):
        return self.driver.find_element(*PlaceOrder.promoinfo)

    def place_order(self):
        return self.driver.find_element(*PlaceOrder.placorder)