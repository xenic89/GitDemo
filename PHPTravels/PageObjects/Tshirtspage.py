from selenium.webdriver.common.by import By


class TshirtsPage:

    def __init__(self, driver):
        self.driver = driver

    add = (By.XPATH, "//span[text()='Add to cart']")
    dname = (By.XPATH, "//li/div/div/h5/a")
    mhover = (By.CSS_SELECTOR, ".product-container")
    rate = (By.CSS_SELECTOR, "li div div div  span[itemprop='price']")
    moveto = (By.CSS_SELECTOR, "div[id='layer_cart'] div[class='clearfix']")


    def Mouse_hover(self):
        return self.driver.find_element(*TshirtsPage.mhover)

    def Addto_Cart(self):
        return self.driver.find_element(*TshirtsPage.add)

    def dress_name(self):
        return self.driver.find_element(*TshirtsPage.dname)

    def shirt_price(self):
        return self.driver.find_element(*TshirtsPage.rate)

    def move_to(self):
        return self.driver.find_element(*TshirtsPage.moveto)