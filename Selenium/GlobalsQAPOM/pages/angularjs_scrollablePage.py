from pages.BasePage import BasePage
from pages.Header_Components import HeaderComponent
from locators.angularjs_scrollable_locators import AngularJSScrollablePageLocators
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
import time
import datetime
import pytest
import re
import json

class AngularJSScrollablePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.angularJSScrollablePageLocators = AngularJSScrollablePageLocators()

    def first_name_search(self, text):
        self.type_into_element(text, AngularJSScrollablePageLocators.first_name_search_locator)

    def global_search(self, text):
        self.type_into_element(text, AngularJSScrollablePageLocators.global_search_locator)

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
        self.type_into_element(user_name, AngularJSScrollablePageLocators.first_name_search_locator)

        # Step 2: Create a dynamic locator for the user's name
        user_locator = self.get_dynamic_locator(AngularJSScrollablePageLocators.user_first_name_in_table_locator, user_name)

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
        self.type_into_element(first_name, AngularJSScrollablePageLocators.first_name_search_locator)

        # Create a dynamic locator for the full name
        user_locator = self.get_dynamic_locator_multiple(AngularJSScrollablePageLocators.user_full_name_locator, first_name, last_name)

        try:
            # Wait for the element to become visible
            self.wait_for_element_to_be_visible(user_locator)
            self.logger.info(f"User '{first_name} {last_name}' found in the table.")
            return True
        except TimeoutException:
            self.logger.error(f"User '{first_name} {last_name}' was not found in the table.")
            return False


    def is_column_sorted_correctly(self, column_name: str, sort_order: str) -> bool:
        """
        Verifies if a column is sorted correctly based on a given order.
        It DOES NOT perform the sort action.
        """
        self.logger.info(f"Verifying {column_name} column is sorted in {sort_order} order.")

        # Step 1: Get the current table data directly from the page
        table_data = self.read_table(
            AngularJSScrollablePageLocators.table_body_locator,
            AngularJSScrollablePageLocators.table_row_locator,
            AngularJSScrollablePageLocators.table_cell_locator
        )

        # Find the index of the column to verify
        header_index = self._get_column_index(column_name)
        if header_index is None:
            self.logger.error(f"Column header '{column_name}' not found.")
            return False

        # Step 2: Extract the data from the target column
        actual_data = [row[header_index] for row in table_data]

        # Step 3: Sort the data programmatically to get the expected order.
        # Use 'float' as the key to sort numerical columns correctly.
        # The 'try-except' block handles cases where the column might contain mixed data.
        try:
            expected_data = sorted(actual_data, key=float, reverse=(sort_order == "descending"))
        except ValueError:
            # If the conversion fails (e.g., a header or non-numerical data is present),
            # fall back to a case-insensitive string sort.
            self.logger.warning(f"Column '{column_name}' contains non-numerical data. Falling back to string sort.")
            expected_data = sorted(actual_data, key=str.lower, reverse=(sort_order == "descending"))

        # Step 4: Compare the actual data with the expected data
        is_sorted = actual_data == expected_data
        if not is_sorted:
            self.logger.error("Data is not sorted as expected.")
            self.logger.error(f"Expected sorted data: {expected_data}")
            self.logger.error(f"Actual sorted data:   {actual_data}")
        else:
            self.logger.info(f"Column '{column_name}' is correctly sorted in {sort_order} order.")
            self.logger.info(f"Expected sorted data: {expected_data}")
            self.logger.info(f"Actual sorted data:   {actual_data}")

        return is_sorted

    def _get_column_index(self, column_name: str) -> int or None:
        """
        Helper method to find the index of a column by its header name.
        """
        # Read headers from the table, assuming a single header row
        header_row_locator = [("xpath", "//thead/tr")]
        header_cell_locator = [("xpath", "./th")]

        headers = self.read_table(
            AngularJSScrollablePageLocators.table_locator,
            header_row_locator,
            header_cell_locator
        )

        if headers and headers[0]:
            try:
                # Find the index of the column name in the list of headers
                return headers[0].index(column_name)
            except ValueError:
                return None
        return None

    def click_header_to_sort(self, header_text: str):
        """Clicks on a table header to trigger a sort."""
        self.logger.info(f"Attempting to click header: {header_text}")

        # Use the dynamic locator to build the specific locator for the header
        header_locator = self.get_dynamic_locator(
            AngularJSScrollablePageLocators.table_header_locator,
            header_text
        )

        # Click the element using your BasePage's click method
        self.element_click(header_locator)

    def find_user_by_scrolling(self, first_name: str, last_name: str, amount: str, max_scrolls: int = 10) -> bool:
        """
        Scrolls the table until it finds the specified user.

        Args:
            first_name (str): The first name of the user to find.
            last_name (str): The last name of the user to find.
            max_scrolls (int): Maximum number of times to scroll to prevent infinite loops.

        Returns:
            bool: True if the user is found, False otherwise.
        """
        self.logger.info(f"Scrolling to find user: {first_name} {last_name}")

        # Use your dynamic locator to find the row

        user_row_locator = self.get_dynamic_locator_multiple(AngularJSScrollablePageLocators.user_full_name_locator, first_name, last_name, amount)


        for i in range(max_scrolls):
            try:
                # Try to find the element
                self.get_element(user_row_locator)
                self.logger.info(f"Found user {first_name} {last_name} after {i} scrolls.")
                return True
            except NoSuchElementException:
                # Element not found, scroll down to load more content
                self.logger.info(f"User not found on scroll {i}. Scrolling down...")
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                # Add a small wait to allow new content to load
                self.driver.implicitly_wait(2)  # Or use an explicit wait
                print("Scrolling")

        self.logger.warning(f"Failed to find user {first_name} {last_name} after {max_scrolls} scrolls.")
        return False
