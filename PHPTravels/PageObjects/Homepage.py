from selenium.webdriver.common.by import By


class Homepage:

    def __init__(self, driver):
        self.driver = driver

    women = (By.CSS_SELECTOR, "a[title='Women']")
    dresses = (By.XPATH, "//div/ul/li/a[text()='Dresses']")
    tshirts = (By.XPATH, "//div/ul/li/a[text()='T-shirts']")
    Signin = (By.CSS_SELECTOR, "div a[class='login']")


    def women_menu(self):   
        return self.driver.find_element(*Homepage.women)

    def dress_menu(self):
        return self.driver.find_element(*Homepage.dresses)

    def tshirts_menu(self):
        return self.driver.find_element(*Homepage.tshirts)

    def sign_in(self):
        return self.driver.find_element(*Homepage.Signin)