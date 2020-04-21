import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.Homepage import Homepage
from Utilities.BaseClass import BaseClass


class Test1(BaseClass):

    def test_1(self):
        self.driver.find_element_by_css_selector("a[title='Women']").click()
        url1 = self.driver.current_url
        assert "http://automationpractice.com/index.php?id_category=3&controller=category" in url1
        self.driver.back()


        self.driver.find_element_by_xpath("//div/ul/li/a[text()='Dresses']").click()
        url2 = self.driver.current_url
        assert "http://automationpractice.com/index.php?id_category=8&controller=category" in url2
        self.driver.back()

        self.driver.find_element_by_xpath("//div/ul/li/a[text()='T-shirts']").click()
        url3 = self.driver.current_url
        assert "http://automationpractice.com/index.php?id_category=5&controller=category" in url3
