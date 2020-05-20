from selenium.webdriver.common.by import By


class Homepage:

    def __init__(self, driver):
        self.driver = driver
    veggies = (By.CSS_SELECTOR, "div div h4")
    beans = (By.XPATH, "//div/div/h4[text()='Beans - 1 Kg']/parent::div/div/button")
    brinjal = (By.XPATH, "//div/div/h4[text()='Brinjal - 1 Kg']/parent::div/div/button")
    cucu = (By.XPATH, "//div/div/h4[text()='Cucumber - 1 Kg']/parent::div/div/button")
    cart = (By.XPATH, "//img[@alt='Cart']")
    checkout = (By.XPATH, "//div/button[text()='PROCEED TO CHECKOUT']")

    def veg_gies(self):
        return self.driver.find_elements(*Homepage.veggies)

    def bea_ns(self):
        return self.driver.find_element(*Homepage.beans)

    def brin_jal(self):
        return self.driver.find_element(*Homepage.brinjal)

    def cu_cu(self):
        return self.driver.find_element(*Homepage.cucu)

    def ca_rt(self):
        return self.driver.find_element(*Homepage.cart)

    def check_out(self):
        return self.driver.find_element(*Homepage.checkout)