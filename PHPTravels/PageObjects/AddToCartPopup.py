from selenium.webdriver.common.by import By


class AddtoCartPopup:

    def __init__(self, driver):
        self.driver = driver

    cartdressname = (By.ID, "layer_cart_product_title")
    quantity = (By.ID, "layer_cart_product_quantity")
    cartprice = (By.ID, "layer_cart_product_price")
    checkout = (By.CSS_SELECTOR, "a[title='Proceed to checkout']")

    def cart_dressname(self):
        return self.driver.find_element(*AddtoCartPopup.cartdressname)

    def quan_tity(self):
        return self.driver.find_element(*AddtoCartPopup.quantity)

    def cart_price(self):
        return self.driver.find_element(*AddtoCartPopup.cartprice)

    def check_out(self):
        return self.driver.find_element(*AddtoCartPopup.checkout)