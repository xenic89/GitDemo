import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Utilities.BaseClass import BaseClass


class test_2(BaseClass):

    def test_two(self):

        self.driver.find_element_by_xpath("//div/ul/li/a[text()='T-shirts']").click()

        dress_name = self.driver.find_element_by_xpath("//li/div/div/h5/a").text
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".product-container")))
        action = ActionChains(self.driver)


        action.move_to_element(self.driver.find_element_by_css_selector(".product-container")).perform()

        price = self.driver.find_element_by_css_selector("li div div div  span[itemprop='price']").text

        self.driver.find_element_by_xpath("//span[text()='Add to cart']").click()

        time.sleep(5)

        action.move_to_element(self.driver.find_element_by_css_selector("div[id='layer_cart'] div[class='clearfix']")).perform()
        cart_dress_name = self.driver.find_element_by_id("layer_cart_product_title").text
        quantity = self.driver.find_element_by_id("layer_cart_product_quantity").text
        cart_price = self.driver.find_element_by_id("layer_cart_product_price").text


        self.driver.find_element_by_css_selector("a[title='Proceed to checkout']").click()

        checkout_dress_name = self.driver.find_element_by_xpath("//a[text()='Faded Short Sleeve T-shirts']").text

        checkout_price = self.driver.find_element_by_xpath("//td[@class='cart_unit']/span/span").text

        assert cart_dress_name == checkout_dress_name == dress_name
        assert price == cart_price == checkout_price

