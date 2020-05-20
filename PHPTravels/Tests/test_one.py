import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#from PageObjects.Homepage import Homepage
#from TestData.HomePageData import HomePageData
#from Utilities.BaseClass import BaseClass
from PHPTravels.PageObjects.Homepage import Homepage
from PHPTravels.TestData import HomePageData

class TestOne(BaseClass):

    def test_first(self):
        log = self.get_Logger()
        homePage = Homepage(self.driver)

        log.info("verifying the main menu item - Women")
        homePage.women_menu().click()
        url1 = self.driver.current_url

        assert HomePageData.url1 in url1
        self.driver.back()

        log.info("verifying the main menu item - Dresses")
        homePage.dress_menu().click()
        url2 = self.driver.current_url
        assert HomePageData.url2 in url2
        self.driver.back()

        log.info("verifying the main menu item - T-Shirts")
        homePage.tshirts_menu().click()
        url3 = self.driver.current_url
        assert HomePageData.url3 in url3
