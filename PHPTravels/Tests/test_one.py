import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.Homepage import Homepage
from TestData.HomePageData import HomePageData
from Utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_first(self):
        homePage = Homepage(self.driver)
        homePage.women_menu().click()
        url1 = self.driver.current_url
        assert HomePageData.url1 in url1
        self.driver.back()

        homePage.dress_menu().click()
        url2 = self.driver.current_url
        assert HomePageData.url2 in url2
        self.driver.back()

        homePage.tshirts_menu().click()
        url3 = self.driver.current_url
        assert HomePageData.url3 in url3
