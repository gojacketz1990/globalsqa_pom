from pages.BasePage import BasePage
from pages.Header_Components import HeaderComponent
from locators.angularjs_simplecalculator_locators import AngularJSSearchFilterPageLocators
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
import time
import datetime
import pytest
import re
import json

class AngularJSSimpleCaculatorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.angularJSSearchFilterPageLocators = AngularJSSearchFilterPageLocators()
