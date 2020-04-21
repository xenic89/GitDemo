import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.AddToCartPopup import AddtoCartPopup
from PageObjects.CheckOutPage import CheckOutPage
from PageObjects.Homepage import Homepage
from PageObjects.Tshirtspage import TshirtsPage
from Utilities.BaseClass import BaseClass


class TestTwo(BaseClass):

    def test_second(self):
        homePage = Homepage(self.driver)
        homePage.tshirts_menu().click()

        tshirtpage = TshirtsPage(self.driver)
        dress_name = tshirtpage.dress_name().text
        wait = WebDriverWait(self.driver, 5)

        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".product-container")))
        action = ActionChains(self.driver)

        action.move_to_element(tshirtpage.Mouse_hover()).perform()

        price = tshirtpage.shirt_price().text

        tshirtpage.Addto_Cart().click()

        time.sleep(5)

        action.move_to_element(tshirtpage.move_to()).perform()
        addtocartPopup = AddtoCartPopup(self.driver)
        cart_dress_name = addtocartPopup.cart_dressname().text
        quantity = addtocartPopup.quan_tity().text
        cart_price = addtocartPopup.cart_price().text

        addtocartPopup.check_out().click()

        checkoutpage = CheckOutPage(self.driver)
        checkout_dress_name = checkoutpage.dress_checkout().text

        checkout_price = checkoutpage.price_checkout().text

        assert cart_dress_name == checkout_dress_name == dress_name
        assert price == cart_price == checkout_price

