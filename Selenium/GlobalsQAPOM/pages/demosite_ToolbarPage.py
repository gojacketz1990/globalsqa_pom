from pages.BasePage import BasePage
from pages.Header_Components import HeaderComponent
from locators.demosite_toolbar_page_locators import DemoToolBarPageLocators
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
import time
import pytest
import re

class DemoToolBarPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.demoToolBarPageLocators = DemoToolBarPageLocators()


    def _click_tab(self, tab_locator: list):
        """
        Internal method to click on a tab.
        """
        self.logger.info(f"Clicking the tab with locator: {tab_locator}")
        self.element_click(tab_locator)
        time.sleep(2)

    def click_toolbar_tab(self):
        self._click_tab(DemoToolBarPageLocators.click_tool_bar_locator)

    def click_splitbutton_tab(self):
        self._click_tab(DemoToolBarPageLocators.click_split_button_tab_locator)

    def select_text_and_font_size(self, textsize: str):
        """
        Selects a font size from the custom dropdown menu.

        Args:
            size (str): The visible text of the font size to select (e.g., '12px').
        """
        self.switch_to_frame(DemoToolBarPageLocators.toolbar_demo_iframe)
        try:
            self.select_all_text_in_element(DemoToolBarPageLocators.document_locator)
            self.logger.info(f"Attempting to select font size: {textsize}")

            # Step 1: Click the dropdown button to open the menu
            self.element_click(DemoToolBarPageLocators.font_size_combobox_locator)

            # Step 2: Get the dynamic locator for the specific font size
            font_size_option_locator = self.get_dynamic_locator(
                DemoToolBarPageLocators.font_size_options_locator,
                textsize
            )
            time.sleep(2)
            # Step 3: Click the desired option using the dynamic locator
            self.element_click(font_size_option_locator)
            self.logger.info(f"Selected font size '{textsize}' successfully.")

        finally:
            self.switch_to_default_content()


    def verify_font_tag_size_attribute(self, expected_size_attribute: str) -> bool:
        """
        Verifies that a nested <font> tag with a specific size attribute is present.

        Args:
            expected_size_attribute (str): The value of the 'size' attribute to check for (e.g., '7').

        Returns:
            bool: True if the font tag with the correct size is found, False otherwise.
        """
        self.switch_to_frame(DemoToolBarPageLocators.toolbar_demo_iframe)
        try:
            self.logger.info(f"Attempting to verify font tag with size='{expected_size_attribute}'.")

            # Get the parent <pre> element
            parent_element = self.get_element(DemoToolBarPageLocators.document_locator)

            # Get the dynamic locator for the nested font tag
            font_tag_locators = self.get_dynamic_locator(
                DemoToolBarPageLocators.font_tag_locator,
                expected_size_attribute
            )

            # Try to get the child element
            try:
                # Find the font tag within the parent element
                font_element = self.get_child_element(parent_element, font_tag_locators)

                # Verify the attribute value
                actual_size = self.get_element_attribute(font_tag_locators, "size")
                if actual_size == expected_size_attribute:
                    self.logger.info(f"Verification successful: Found <font size='{actual_size}'> tag.")
                    return True
                else:
                    self.logger.warning(f"Verification failed: Found <font size='{actual_size}'> instead of '{expected_size_attribute}'.")
                    return False
            except NoSuchElementException:
                self.logger.warning(f"Verification failed: Could not find <font size='{expected_size_attribute}'> tag.")
                return False
        finally:
            self.switch_to_default_content()

    def select_action_from_dropdown(self, action_text: str):
        """
        Clicks the 'Open/Save/Delete' dropdown button and selects a specified option.

        Args:
            action_text (str): The visible text of the option to select
                               (e.g., 'Open...', 'Save', 'Delete').
        """
        self.switch_to_frame(self.demoToolBarPageLocators.splitbutton_demo_iframe)
        try:
            self.logger.info(f"Attempting to select action: '{action_text}' from dropdown.")

            # Step 1: Click the visible dropdown button to open the menu
            self.element_click(self.demoToolBarPageLocators.drop_down_button_locator)
            time.sleep(1) # Give a short pause for the menu to appear

            # Step 2: Get the dynamic locator for the specific option
            option_locators = self.get_dynamic_locator(
                self.demoToolBarPageLocators.action_dropdown_option_locator,
                action_text
            )

            # Step 3: Click the desired option
            self.element_click(option_locators)
            self.logger.info(f"Successfully selected action '{action_text}'.")

        finally:
            self.switch_to_default_content()

    def click_run_last_option_button(self):
        self.switch_to_frame(self.demoToolBarPageLocators.splitbutton_demo_iframe)
        try:
            # Step 1: Click the visible dropdown button to open the menu
            self.element_click(self.demoToolBarPageLocators.run_last_option_button_locator)
            time.sleep(1) # Give a short pause for the menu to appear

        finally:
            self.switch_to_default_content()

    def get_all_output_texts(self) -> list[str]:
        """
        Retrieves the text from all items in the output list.
        """
        self.switch_to_frame(self.demoToolBarPageLocators.splitbutton_demo_iframe)
        try:
            # Find all <li> elements that match the locator
            output_elements = self.get_elements(self.demoToolBarPageLocators.output_list_items_locator)

            # Extract the text from each element and store it in a list
            output_texts = [element.text for element in output_elements]

            self.logger.info(f"Captured all output texts: {output_texts}")
            return output_texts
        finally:
            self.switch_to_default_content()
