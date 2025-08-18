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

    def is_user_present_in_table(self, user_name: str) -> bool:
        """
        Searches for a user by name and verifies they are present in the filtered table.

        Args:
            user_name (str): The name to search for.

        Returns:
            bool: True if the user is found, False otherwise.
        """
        self.logger.info(f"Searching for user: {user_name}")

        # Step 1: Type the name into the search box
        self.type_into_element(user_name, AngularJSWebTablePageLocators.first_name_search_locator)

        # Step 2: Create a dynamic locator for the user's name
        user_locator = self.get_dynamic_locator(AngularJSWebTablePageLocators.user_first_name_in_table_locator, user_name)

        # Step 3: Wait for the element to be visible
        try:
            self.wait_for_element_to_be_visible(user_locator)
            self.logger.info(f"User '{user_name}' found in the table.")
            return True
        except TimeoutException:
            self.logger.error(f"User '{user_name}' was not found in the table after searching.")
            return False

    def is_user_full_name_present_in_table(self, first_name: str, last_name: str) -> bool:
        """
        Searches for a user by their full name and verifies they are present in the filtered table.

        Args:
            first_name (str): The user's first name.
            last_name (str): The user's last name.

        Returns:
            bool: True if the user is found, False otherwise.
        """
        self.logger.info(f"Searching for user: {first_name} {last_name}")

        # Type the first name into the search box
        self.type_into_element(first_name, AngularJSWebTablePageLocators.first_name_search_locator)

        # Create a dynamic locator for the full name
        user_locator = self.get_dynamic_locator_multiple(AngularJSWebTablePageLocators.user_full_name_locator, first_name, last_name)

        try:
            # Wait for the element to become visible
            self.wait_for_element_to_be_visible(user_locator)
            self.logger.info(f"User '{first_name} {last_name}' found in the table.")
            return True
        except TimeoutException:
            self.logger.error(f"User '{first_name} {last_name}' was not found in the table.")
            return False
