import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.Homepage import Homepage
from Utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_first(self):
        homePage = Homepage(self.driver)
        homePage.women_menu().click()
        url1 = self.driver.current_url
        assert "http://automationpractice.com/index.php?id_category=3&controller=category" in url1
        self.driver.back()

        homePage.dress_menu().click()
        url2 = self.driver.current_url
        assert "http://automationpractice.com/index.php?id_category=8&controller=category" in url2
        self.driver.back()

        homePage.tshirts_menu().click()
        url3 = self.driver.current_url
        assert "http://automationpractice.com/index.php?id_category=5&controller=category" in url3
