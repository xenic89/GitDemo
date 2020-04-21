import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Utilities.BaseClass import BaseClass


class test_3(BaseClass):

    def test_three(self):

        #login
        self.driver.find_element_by_css_selector("div a[class='login']").click()
        self.driver.find_element_by_id("email").send_keys("din@abc.com")
        self.driver.find_element_by_id("passwd").send_keys("123456")
        self.driver.find_element_by_id("SubmitLogin").click()
        self.driver.find_element_by_xpath("//div/a/img[@alt='My Store']").click()



        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        footer_menu = self.driver.find_elements_by_css_selector("section[class*='footer'] h4")
        footer_headings = []

        for i in footer_menu:
            footer_headings.append(i.text)

        footer_categories = self.driver.find_element_by_xpath("//*[contains(@class, 'footer')]/h4[text()='Categories']/parent::section/div/div/ul/li/a").text

        footer_info = self.driver.find_elements_by_xpath("//*[contains(@class, 'footer')]/h4[text()='Information']/parent::section/ul/li")
        footer_information = []

        for i in footer_info:
            footer_information.append(i.text)

        footer_myacc = self.driver.find_elements_by_xpath("//*[contains(@class, 'footer')]/h4/a/parent::h4/parent::section/div/ul/li")
        footer_myaccount = []

        for i in footer_myacc:
            footer_myaccount.append(i.text)

        headings = ['Categories', 'Information', 'My account', 'Store information']
        categories = "Women"
        information = ['Specials', 'New products', 'Best sellers', 'Our stores', 'Contact us', 'Terms and conditions of use', 'About us', 'Sitemap']
        myaccount = ['My orders', 'My credit slips', 'My addresses', 'My personal info', 'Sign out']

        assert headings == footer_headings
        assert categories == footer_categories
        assert information == footer_information
        assert myaccount == footer_myaccount

        # Categories - Women
        self.driver.find_element_by_xpath("//*[contains(@class, 'footer')]/h4[text()='Categories']/parent::section/div/div/ul/li/a").click()
        assert self.driver.current_url == "http://automationpractice.com/index.php?id_category=3&controller=category"
        self.driver.back()

        # Information - Specials
        self.driver.find_element_by_xpath("//*[contains(@class, 'footer')]/h4[text()='Information']/parent::section/ul/li/a[@title='Specials']").click()
        assert self.driver.current_url == "http://automationpractice.com/index.php?controller=prices-drop"
        self.driver.back()

        # Information - New products
        self.driver.find_element_by_xpath("//*[contains(@class, 'footer')]/h4[text()='Information']/parent::section/ul/li/a[@title='New products']").click()
        assert self.driver.current_url == "http://automationpractice.com/index.php?controller=new-products"
        self.driver.back()

        # Information - Best sellers
        self.driver.find_element_by_xpath("//*[contains(@class, 'footer')]/h4[text()='Information']/parent::section/ul/li/a[@title='Best sellers']").click()
        assert self.driver.current_url == "http://automationpractice.com/index.php?controller=best-sales"
        self.driver.back()

        # Information - Our stores
        self.driver.find_element_by_xpath("//*[contains(@class, 'footer')]/h4[text()='Information']/parent::section/ul/li/a[@title='Our stores']").click()
        assert self.driver.current_url == "http://automationpractice.com/index.php?controller=stores"
        self.driver.back()

        # Information - Contact us
        self.driver.find_element_by_xpath("//*[contains(@class, 'footer')]/h4[text()='Information']/parent::section/ul/li/a[@title='Contact us']").click()
        assert self.driver.current_url == "http://automationpractice.com/index.php?controller=contact"
        self.driver.back()

        # Information - Terms & conditions
        self.driver.find_element_by_xpath("//*[contains(@class, 'footer')]/h4[text()='Information']/parent::section/ul/li/a[@title='Terms and conditions of use']").click()
        assert self.driver.current_url == "http://automationpractice.com/index.php?id_cms=3&controller=cms"
        self.driver.back()

        # Information - About us
        self.driver.find_element_by_xpath("//*[contains(@class, 'footer')]/h4[text()='Information']/parent::section/ul/li/a[@title='About us']").click()
        assert self.driver.current_url == "http://automationpractice.com/index.php?id_cms=4&controller=cms"
        self.driver.back()

        # Information -  Sitemap
        self.driver.find_element_by_xpath("//*[contains(@class, 'footer')]/h4[text()='Information']/parent::section/ul/li/a[@title='Sitemap']").click()
        assert self.driver.current_url == "http://automationpractice.com/index.php?controller=sitemap"
        self.driver.back()

        # My account - My orders
        self.driver.find_element_by_xpath("//*[contains(@class, 'footer')]/h4/a/parent::h4/parent::section/div/ul/li/a[@title='My orders']").click()
        assert self.driver.current_url == "http://automationpractice.com/index.php?controller=history"
        self.driver.back()

        # My account - My credit slips
        self.driver.find_element_by_xpath("//*[contains(@class, 'footer')]/h4/a/parent::h4/parent::section/div/ul/li/a[@title='My credit slips']").click()
        assert self.driver.current_url == "http://automationpractice.com/index.php?controller=order-slip"
        self.driver.back()

        # My account - My addresses
        self.driver.find_element_by_xpath("//*[contains(@class, 'footer')]/h4/a/parent::h4/parent::section/div/ul/li/a[@title='My addresses']").click()
        assert self.driver.current_url == "http://automationpractice.com/index.php?controller=addresses"
        self.driver.back()

        # My account - My personal info
        self.driver.find_element_by_xpath("//*[contains(@class, 'footer')]/h4/a/parent::h4/parent::section/div/ul/li/a[@title='Manage my personal information']").click()
        assert self.driver.current_url == "http://automationpractice.com/index.php?controller=identity"
        self.driver.back()

        self.driver.find_element_by_xpath("//*[contains(@class, 'footer')]/h4/a/parent::h4/parent::section/div/ul/li/a[@title='Sign out']").click()
        assert self.driver.current_url == "http://automationpractice.com/index.php"