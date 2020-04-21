import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.Footer import FooterSection
from PageObjects.Homepage import Homepage
from PageObjects.SignIn import SignIn
from Utilities.BaseClass import BaseClass


class TestThree(BaseClass):

    def test_third(self):
        homepage = Homepage(self.driver)
        signin = SignIn(self.driver)
        homepage.sign_in().click()
        signin.user_field().send_keys("din@abc.com")
        signin.pwd_field().send_keys("123456")
        signin.sub_mit().click()
        signin.homepage_button().click()

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        footerpage = FooterSection(self.driver)
        footer_menu = footerpage.footer_menu()
        footer_headings = []

        for i in footer_menu:
            footer_headings.append(i.text)

        footer_categories = footerpage.footer_category().text

        footer_info = footerpage.footer_info()
        footer_information = []

        for i in footer_info:
            footer_information.append(i.text)

        footer_myacc = footerpage.footer_acc()
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
        footerpage.wo_men().click()
        assert self.driver.current_url == "http://automationpractice.com/index.php?id_category=3&controller=category"
        self.driver.back()

        # Information - Specials
        footerpage.spec_ial().click()
        assert self.driver.current_url == "http://automationpractice.com/index.php?controller=prices-drop"
        self.driver.back()

        # Information - New products
        footerpage.new_products().click()
        assert self.driver.current_url == "http://automationpractice.com/index.php?controller=new-products"
        self.driver.back()

        # Information - Best sellers
        footerpage.best_sellers().click()
        assert self.driver.current_url == "http://automationpractice.com/index.php?controller=best-sales"
        self.driver.back()

        # Information - Our stores
        footerpage.our_stores().click()
        assert self.driver.current_url == "http://automationpractice.com/index.php?controller=stores"
        self.driver.back()

        # Information - Contact us
        footerpage.contact_us().click()
        assert self.driver.current_url == "http://automationpractice.com/index.php?controller=contact"
        self.driver.back()

        # Information - Terms & conditions
        footerpage.terms_conditions().click()
        assert self.driver.current_url == "http://automationpractice.com/index.php?id_cms=3&controller=cms"
        self.driver.back()

        # Information - About us
        footerpage.about_us().click()
        assert self.driver.current_url == "http://automationpractice.com/index.php?id_cms=4&controller=cms"
        self.driver.back()

        # Information -  Sitemap
        footerpage.site_map().click()
        assert self.driver.current_url == "http://automationpractice.com/index.php?controller=sitemap"
        self.driver.back()

        # My account - My orders
        footerpage.my_orders().click()
        assert self.driver.current_url == "http://automationpractice.com/index.php?controller=history"
        self.driver.back()

        # My account - My credit slips
        footerpage.credit_slip().click()
        assert self.driver.current_url == "http://automationpractice.com/index.php?controller=order-slip"
        self.driver.back()

        # My account - My addresses
        footerpage.my_address().click()
        assert self.driver.current_url == "http://automationpractice.com/index.php?controller=addresses"
        self.driver.back()

        # My account - My personal info
        footerpage.personal_info().click()
        assert self.driver.current_url == "http://automationpractice.com/index.php?controller=identity"
        self.driver.back()

        footerpage.sign_out().click()
        assert self.driver.current_url == "http://automationpractice.com/index.php"