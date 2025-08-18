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

    def is_payment_page_displayed(self):
        """Checks if the 'Interests' page is displayed by verifying its unique header."""
        self.wait_for_element_to_be_visible(AngularJSMultiformPageLocators.question_text_locator)
        return True

    def get_json_submitted(self):
        return self.get_json_data_from_element(AngularJSMultiformPageLocators.json_data_locator)

    def select_radio_button_by_value(self, value):
        """
        Selects a radio button based on its 'value' attribute.
        """
        # Create the specific locator using your get_dynamic_locator method
        radio_locator = self.get_dynamic_locator(AngularJSMultiformPageLocators.console_radio_buttons, value)

        # Click the radio button
        self.element_click(radio_locator)

    def is_radio_button_selected_by_value(self, value):
        """
        Checks if a specific radio button is selected based on its value.

        Args:
            value (str): The 'value' attribute of the radio button (e.g., 'xbox').

        Returns:
            bool: True if the radio button is selected, False otherwise.
        """
        radio_locator = self.get_dynamic_locator(AngularJSMultiformPageLocators.console_radio_buttons, value)
        return self.is_element_selected(radio_locator)

    def get_payment_success_message(self):
        """
        Retrieves the text of the payment success message.
        """
        # Wait for the element to be visible to ensure it has loaded
        element = self.wait_for_element_to_be_visible(AngularJSMultiformPageLocators.success_header_locator)
        return element.text
