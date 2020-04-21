from selenium.webdriver.common.by import By


class Homepage():

    def __init__(self, driver):
        self.driver = driver

    women = (By.CSS_SELECTOR, "a[title='Women']")
    dresses = (By.XPATH, "//div/ul/li/a[text()='Dresses']")
    tshirts = (By.XPATH, "//div/ul/li/a[text()='T-shirts']")


    def women_menu(self):
        return self.driver.find_element(*Homepage.women)

    def dress_menu(self):
        return self.driver.find_element(*Homepage.dresses)

    def tshirts(self):
        return self.driver.find_element(*Homepage.tshirts)
