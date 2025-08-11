from pages.BasePage import BasePage
from locators.demosite_draggable_box_page_locators import DemoDraggableBoxPageLocators
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
import time
import datetime
import pytest
import re

class DemoDraggableBoxPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.demoDraggableBoxPageLocators = DemoDraggableBoxPageLocators()


    def _click_tab(self, tab_locator: list):
        """
        Internal method to click on a tab.
        """
        self.logger.info(f"Clicking the tab with locator: {tab_locator}")
        self.element_click(tab_locator)
        time.sleep(2)
