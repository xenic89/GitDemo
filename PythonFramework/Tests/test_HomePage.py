import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from pageObjects.HomePage import HomePage
from testData.HomePageData import HomePageData

from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmit(self, getData):
        homePage = HomePage(self.driver)
        homePage.enter_Name().send_keys(getData["FName"])

        homePage.enter_Email().send_keys(getData["LName"])

        homePage.check_box().click()

        self.Dropdown(homePage.drop_down(), getData["Gender"])

        homePage.Submit_form().click()

        message = homePage.succ_text()

        assert "success" in message
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("TC2"))
    def getData(self, request):
        return request.param
