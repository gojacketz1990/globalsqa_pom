from pages.BasePage import BasePage
from pages.Header_Components import HeaderComponent
from locators.demosite_sample_page_locators import DemoSamplePageLocators
from selenium.common.exceptions import TimeoutException
import time
import pytest
import re

class DemoSamplePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.demoSamplePageLocators = DemoSamplePageLocators()
