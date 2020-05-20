from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from PageObject.CheckOut import CheckOut
from PageObject.Homepage import Homepage
from PageObject.PlaceOrder import PlaceOrder
from Utilities.Baseclass import Baseclass


class TestNormalflow(Baseclass):


    def test_one(self):
        log = self.get_Logger()
        homepage = Homepage(self.driver)
        placeorder = PlaceOrder(self.driver)
        checkout = CheckOut(self.driver)

        veggies = homepage.veg_gies()
        log.info("Collecting all vegetable names in a list")
        for i in veggies:
            print(i.text)
            if i.text == 'Beans - 1 Kg':
                homepage.bea_ns().click()
            if i.text == 'Brinjal - 1 Kg':
                homepage.brin_jal().click()
            if i.text == 'Cucumber - 1 Kg':
                homepage.cu_cu().click()
        log.info("Clicking only on Beans, Brinjal and Cucumber")

        homepage.ca_rt().click()
        log.info("Verifying the cart is added with the required items")
        homepage.check_out().click()
        log.info("After confirmation, proceed to place order")
        self.verifyLinkPresence("promoCode")

        placeorder.promo_code().send_keys("rahulshettyacademy")
        placeorder.promo_btn().click()
        log.info("Entering discount code for verifying discount")

        self.verifyLinkPresence("promoInfo")

        assert "Code applied ..!" == placeorder.promo_info().text
        log.info("Verifying the promom code success message")
        placeorder.place_order().click()

        self.dropdown("div select")

        log.info("Selecting current country for address")
        checkout.agree_btn().click()
        checkout.pro_btn().click()
        log.info("Successfully Placed Order")

