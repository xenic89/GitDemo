import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Utilities.BaseClass import BaseClass


class Test3(BaseClass):

    def test_3(self):
        driver = webdriver.Chrome(executable_path="D:\\PyCharm Community Edition 2019.3.3\\chromedriver.exe")

        driver.get("http://automationpractice.com/index.php")
        driver.maximize_window()

        #login
        driver.find_element_by_css_selector("div a[class='login']").click()
        driver.find_element_by_id("email").send_keys("din@abc.com")
        driver.find_element_by_id("passwd").send_keys("123456")
        driver.find_element_by_id("SubmitLogin").click()
        driver.find_element_by_xpath("//div/a/img[@alt='My Store']").click()



        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        footer_menu = driver.find_elements_by_css_selector("section[class*='footer'] h4")
        footer_headings = []

        for i in footer_menu:
            footer_headings.append(i.text)

        footer_categories = driver.find_element_by_xpath("//*[contains(@class, 'footer')]/h4[text()='Categories']/parent::section/div/div/ul/li/a").text

        footer_info = driver.find_elements_by_xpath("//*[contains(@class, 'footer')]/h4[text()='Information']/parent::section/ul/li")
        footer_information = []

        for i in footer_info:
            footer_information.append(i.text)

        footer_myacc = driver.find_elements_by_xpath("//*[contains(@class, 'footer')]/h4/a/parent::h4/parent::section/div/ul/li")
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
        driver.find_element_by_xpath("//*[contains(@class, 'footer')]/h4[text()='Categories']/parent::section/div/div/ul/li/a").click()
        assert driver.current_url == "http://automationpractice.com/index.php?id_category=3&controller=category"
        driver.back()

        # Information - Specials
        driver.find_element_by_xpath("//*[contains(@class, 'footer')]/h4[text()='Information']/parent::section/ul/li/a[@title='Specials']").click()
        assert driver.current_url == "http://automationpractice.com/index.php?controller=prices-drop"
        driver.back()

        # Information - New products
        driver.find_element_by_xpath("//*[contains(@class, 'footer')]/h4[text()='Information']/parent::section/ul/li/a[@title='New products']").click()
        assert driver.current_url == "http://automationpractice.com/index.php?controller=new-products"
        driver.back()

        # Information - Best sellers
        driver.find_element_by_xpath("//*[contains(@class, 'footer')]/h4[text()='Information']/parent::section/ul/li/a[@title='Best sellers']").click()
        assert driver.current_url == "http://automationpractice.com/index.php?controller=best-sales"
        driver.back()

        # Information - Our stores
        driver.find_element_by_xpath("//*[contains(@class, 'footer')]/h4[text()='Information']/parent::section/ul/li/a[@title='Our stores']").click()
        assert driver.current_url == "http://automationpractice.com/index.php?controller=stores"
        driver.back()

        # Information - Contact us
        driver.find_element_by_xpath("//*[contains(@class, 'footer')]/h4[text()='Information']/parent::section/ul/li/a[@title='Contact us']").click()
        assert driver.current_url == "http://automationpractice.com/index.php?controller=contact"
        driver.back()

        # Information - Terms & conditions
        driver.find_element_by_xpath("//*[contains(@class, 'footer')]/h4[text()='Information']/parent::section/ul/li/a[@title='Terms and conditions of use']").click()
        assert driver.current_url == "http://automationpractice.com/index.php?id_cms=3&controller=cms"
        driver.back()

        # Information - About us
        driver.find_element_by_xpath("//*[contains(@class, 'footer')]/h4[text()='Information']/parent::section/ul/li/a[@title='About us']").click()
        assert driver.current_url == "http://automationpractice.com/index.php?id_cms=4&controller=cms"
        driver.back()

        # Information -  Sitemap
        driver.find_element_by_xpath("//*[contains(@class, 'footer')]/h4[text()='Information']/parent::section/ul/li/a[@title='Sitemap']").click()
        assert driver.current_url == "http://automationpractice.com/index.php?controller=sitemap"
        driver.back()

        # My account - My orders
        driver.find_element_by_xpath("//*[contains(@class, 'footer')]/h4/a/parent::h4/parent::section/div/ul/li/a[@title='My orders']").click()
        assert driver.current_url == "http://automationpractice.com/index.php?controller=history"
        driver.back()

        # My account - My credit slips
        driver.find_element_by_xpath("//*[contains(@class, 'footer')]/h4/a/parent::h4/parent::section/div/ul/li/a[@title='My credit slips']").click()
        assert driver.current_url == "http://automationpractice.com/index.php?controller=order-slip"
        driver.back()

        # My account - My addresses
        driver.find_element_by_xpath("//*[contains(@class, 'footer')]/h4/a/parent::h4/parent::section/div/ul/li/a[@title='My addresses']").click()
        assert driver.current_url == "http://automationpractice.com/index.php?controller=addresses"
        driver.back()

        # My account - My personal info
        driver.find_element_by_xpath("//*[contains(@class, 'footer')]/h4/a/parent::h4/parent::section/div/ul/li/a[@title='Manage my personal information']").click()
        assert driver.current_url == "http://automationpractice.com/index.php?controller=identity"
        driver.back()

        driver.find_element_by_xpath("//*[contains(@class, 'footer')]/h4/a/parent::h4/parent::section/div/ul/li/a[@title='Sign out']").click()
        assert driver.current_url == "http://automationpractice.com/index.php"


        driver.close()