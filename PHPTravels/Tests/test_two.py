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
        log = self.get_Logger()
        homePage = Homepage(self.driver)
        homePage.tshirts_menu().click()

        tshirtpage = TshirtsPage(self.driver)
        dress_name = tshirtpage.dress_name().text
        log.info("Name of tshirt in homepage is : "+dress_name)


        self.verifyLinkPresence(".product-container")

        self.actionClass(tshirtpage.Mouse_hover())
        #action = ActionChains(self.driver)

        #action.move_to_element(tshirtpage.Mouse_hover()).perform()

        price = tshirtpage.shirt_price().text
        log.info("Price of tshirt in homepage is : "+price)

        tshirtpage.Addto_Cart().click()

        time.sleep(5)
        self.actionClass(tshirtpage.move_to())
        #action.move_to_element(tshirtpage.move_to()).perform()
        addtocartPopup = AddtoCartPopup(self.driver)

        cart_dress_name = addtocartPopup.cart_dressname().text
        log.info("Name of tshirt in Cart pop-up is : "+cart_dress_name)

        cart_quantity = addtocartPopup.quan_tity().text
        log.info("Quantity of tshirt in Cart pop-up is : "+cart_quantity)

        cart_price = addtocartPopup.cart_price().text
        log.info("Price of tshirt in Cart pop-up is : "+cart_price)

        addtocartPopup.check_out().click()

        checkoutpage = CheckOutPage(self.driver)
        checkout_dress_name = checkoutpage.dress_checkout().text
        log.info("Name of tshirt in checkout page is : "+checkout_dress_name)


        checkout_price = checkoutpage.price_checkout().text
        log.info("Price of tshirt in checkout page is : "+checkout_price)

        #checkout_quantity = checkoutpage.quantity_checkout()
        #log.info("Quantity of tshirt in checkout page is : "+checkout_quantity)

        assert cart_dress_name == checkout_dress_name == dress_name
        assert price == cart_price == checkout_price
        #assert cart_quantity == checkout_quantity

