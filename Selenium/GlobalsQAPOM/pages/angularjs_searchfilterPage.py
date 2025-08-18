from pages.BasePage import BasePage
from pages.Header_Components import HeaderComponent
from locators.angularjs_searchfilter_locators import AngularJSSearchFilterPageLocators
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
import time
import datetime
import pytest
import re
import json

class AngularJSSearchFilterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.angularJSSearchFilterPageLocators = AngularJSSearchFilterPageLocators()


    def _click_tab(self, tab_locator: list):
        """
        Internal method to click on a tab.
        """
        self.logger.info(f"Clicking the tab with locator: {tab_locator}")
        self.element_click(tab_locator)
        time.sleep(2)
