from pages.BasePage import BasePage
from pages.Header_Components import HeaderComponent
from locators.angularjs_multiform_locators import AngularJSMultiformPageLocators
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
import time
import datetime
import pytest
import re
import json

class AngularJSMultiFormPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.angularJSMultiformPageLocators = AngularJSMultiformPageLocators()


    def _click_tab(self, tab_locator: list):
        """
        Internal method to click on a tab.
        """
        self.logger.info(f"Clicking the tab with locator: {tab_locator}")
        self.element_click(tab_locator)
        time.sleep(2)

    def enter_name(self,name):
        self.type_into_element(name, AngularJSMultiformPageLocators.name_text_box_locator)

    def enter_email(self,email):
        self.type_into_element(email, AngularJSMultiformPageLocators.email_text_box_locator)

    def click_next_section_button(self):
        self.element_click(AngularJSMultiformPageLocators.next_section_button_locator)


    def is_interests_page_displayed(self):
        """Checks if the 'Interests' page is displayed by verifying its unique header."""
        self.wait_for_element_to_be_visible(AngularJSMultiformPageLocators.question_text_locator)
        return True

    def get_json_submitted(self):
        return self.get_json_data_from_element(AngularJSMultiformPageLocators.json_data_locator)

