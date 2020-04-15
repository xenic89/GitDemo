import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.HomePage import HomePage
from pageObjects.confirmPage import confirmPage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.get_Logger()
        homePage = HomePage(self.driver)
        checkoutPage = homePage.shopItems()
        log.info("getting all the cart items")
        products = checkoutPage.Allproducts()
        confirm_page = confirmPage(self.driver)


        for i in products:
            pname = checkoutPage.Product_Name()
            log.info("card Text : ", pname)
            #pname = i.find_element_by_xpath("div/h4/a").text
            if pname == "Blackberry":
                i.checkOutPage.AddtoCart()


        confirm_page = checkoutPage.CheckOutItems()
        log.info("Entering country name as India")
        confirm_page.confirmPage().click()
        confirm_page.coun_try().send_keys("ind")
        self.verifyElementPresence("//a[text()='India']")
        confirm_page.country_appear().click()

        confirm_page.check_box().click()
        confirm_page.purch_Button().click()
        txt = confirm_page.Suc_text()
        log.info("Text received from application is :",txt)

        assert "Success! Thank you!" in txt

        self.driver.get_screenshot_as_file("screen.png")