import inspect

import pytest
import logging
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class Baseclass:

    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 7).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, text)))

    def dropdown(self, text):
        element = Select(self.driver.find_element_by_css_selector(text)).select_by_value("India")

    def get_Logger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s ")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger