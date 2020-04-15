from selenium.webdriver.common.by import By

from pageObjects.confirmPage import confirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    products = (By.XPATH, "//div[@class='card h-100']")
    ProductName = (By.XPATH, "//div[@class='card h-100']/div/h4/a")
    AddtoCart = (By.XPATH, "//div[@class='card h-100']/div/button")
    checkOut = (By.CSS_SELECTOR, "a[class*='nav-link btn']")

    def Allproducts(self):
        return self.driver.find_elements(*CheckOutPage.products)

    def Product_Name(self):
        return self.driver.find_element(*CheckOutPage.ProductName).text

    def AddtoCart(self):
        return self.driver.find_elements(*CheckOutPage.AddtoCart)

    def CheckOutItems(self):
        self.driver.find_element(*CheckOutPage.checkOut).click()
        confirm_page = confirmPage(self.driver)
        return confirm_page
