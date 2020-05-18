import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.Footer import FooterSection
from PageObjects.Homepage import Homepage
from PageObjects.SignIn import SignIn
from TestData.FooterData import FooterData
from TestData.HomePageData import HomePageData
from Utilities.BaseClass import BaseClass


class TestThree(BaseClass):

    def test_third(self, getData):
        log = self.get_Logger()
        homepage = Homepage(self.driver)
        signin = SignIn(self.driver)
        homepage.sign_in().click()
        signin.user_field().send_keys(getData["email"])
        log.info("User logging in :" + getData["email"])
        signin.pwd_field().send_keys(getData["password"])
        log.info("User logging in :" + getData["password"])
        signin.sub_mit().click()
        signin.homepage_button().click()

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        footerpage = FooterSection(self.driver)
        footer_menu = footerpage.footer_menu()
        footer_headings = []

        for i in footer_menu:
            footer_headings.append(i.text)
        log.info(" footer headings ")

        footer_categories = footerpage.footer_category().text
        log.info(" Sub-headers under categories : "+footer_categories)


        footer_info = footerpage.footer_info()
        footer_information = []

        for i in footer_info:
            footer_information.append(i.text)
        log.info("All sub headings under Information")

        footer_myacc = footerpage.footer_acc()
        footer_myaccount = []


        for i in footer_myacc:
            footer_myaccount.append(i.text)
        log.info("All sub headings under Account")

        assert FooterData.headings == footer_headings
        assert FooterData.categories == footer_categories
        assert FooterData.information == footer_information
        assert FooterData.myaccount == footer_myaccount

        # Categories - Women
        log.info("Verifying footer links")
        footerpage.wo_men().click()
        assert self.driver.current_url == FooterData.women
        self.driver.back()

        # Information - Specials
        footerpage.spec_ial().click()
        assert self.driver.current_url == FooterData.specials
        self.driver.back()

        # Information - New products
        footerpage.new_products().click()
        assert self.driver.current_url == FooterData.newproducts
        self.driver.back()

        # Information - Best sellers
        footerpage.best_sellers().click()
        assert self.driver.current_url == FooterData.bestsellers
        self.driver.back()

        # Information - Our stores
        footerpage.our_stores().click()
        assert self.driver.current_url == FooterData.ourstores
        self.driver.back()

        # Information - Contact us
        footerpage.contact_us().click()
        assert self.driver.current_url == FooterData.contactus
        self.driver.back()

        # Information - Terms & conditions
        footerpage.terms_conditions().click()
        assert self.driver.current_url == FooterData.termsconditions
        self.driver.back()

        # Information - About us
        footerpage.about_us().click()
        assert self.driver.current_url == FooterData.aboutus
        self.driver.back()

        # Information -  Sitemap
        footerpage.site_map().click()
        assert self.driver.current_url == FooterData.sitemap
        self.driver.back()

        # My account - My orders
        footerpage.my_orders().click()
        assert self.driver.current_url == FooterData.myorders
        self.driver.back()

        # My account - My credit slips
        footerpage.credit_slip().click()
        assert self.driver.current_url == FooterData.creditslips
        self.driver.back()

        # My account - My addresses
        footerpage.my_address().click()
        assert self.driver.current_url == FooterData.myaddresses
        self.driver.back()

        # My account - My personal info
        footerpage.personal_info().click()
        assert self.driver.current_url == FooterData.myinfo
        self.driver.back()

        footerpage.sign_out().click()
        assert self.driver.current_url == FooterData.signouthomepage
        time.sleep(5)
    @pytest.fixture(params=HomePageData.test_Homepage_data)
    def getData(self, request):
        return request.param
