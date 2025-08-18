from pages.BasePage import BasePage
from pages.Header_Components import HeaderComponent
from locators.angularjs_webtable_locators import AngularJSWebTablePageLocators
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
import time
import datetime
import pytest
import re
import json

class AngularJSWebTablePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.angularJSWebTablePageLocators = AngularJSWebTablePageLocators()


    def _click_tab(self, tab_locator: list):
        """
        Internal method to click on a tab.
        """
        self.logger.info(f"Clicking the tab with locator: {tab_locator}")
        self.element_click(tab_locator)
        time.sleep(2)

    def first_name_search(self, text):
        self.type_into_element(text, AngularJSWebTablePageLocators.first_name_search_locator)

    def global_search(self, text):
        self.type_into_element(text, AngularJSWebTablePageLocators.global_search_locator)
