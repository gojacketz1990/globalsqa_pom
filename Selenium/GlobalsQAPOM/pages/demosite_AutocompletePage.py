from pages.BasePage import BasePage
from pages.Header_Components import HeaderComponent
from locators.demosite_autocomplete_locators import DemoAutocompletePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
import time
import pytest

class DemoAutocompletePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.demoAutocompletePageLocators = DemoAutocompletePageLocators()

    def _click_tab(self, tab_locator: list):
        """
        Internal method to click on a tab.
        """
        self.logger.info(f"Clicking the tab with locator: {tab_locator}")
        self.element_click(tab_locator)

    def click_categories_tab(self):
        self._click_tab(DemoAutocompletePageLocators.categories_tab)

    def click_combobox_tab(self):
        self._click_tab(DemoAutocompletePageLocators.combobox_tab)

    def enter_text_into_search(self, text):
        """
        Types text into the autocomplete input field and waits for the suggestions to appear.
        """
        try:
            # Step 1: Switch to the iframe
            self.switch_to_frame(DemoAutocompletePageLocators.categories_demo_iframe)

            # Step 2: Type the text into the search box
            self.type_into_element(text, DemoAutocompletePageLocators.search_box_locator)

            # Step 3: Wait for the autocomplete suggestions to appear
            # This is the correct element to wait for after typing.
            self.wait_for_element_to_be_visible(
                DemoAutocompletePageLocators.autocomplete_suggestions_locator,
                timeout=5
            )
            return True

        except Exception as e:
            # If any error occurs (e.g., suggestions don't appear in time)
            print(f"An error occurred: {e}")
            return False

        finally:
            # Step 4: Always switch back to the default content
            self.switch_to_default_content()



    def get_autocomplete_suggestions(self):
        """
        Waits for and returns a list of all visible autocomplete suggestions.
        Handles the potential for stale elements as the list updates.
        """
        self.switch_to_frame(DemoAutocompletePageLocators.categories_demo_iframe)

        try:
            return self.wait_for_all_elements_to_be_visible(DemoAutocompletePageLocators.autocomplete_suggestions_locator)
        except TimeoutException:
            self.logger.info("No autocomplete suggestions appeared within the timeout.")
            return []
        finally:
            # 3. Always switch back to the default content
            self.switch_to_default_content()



    def select_suggestion_by_text(self, text):
        """
        Switches to the iframe, finds and clicks a specific autocomplete suggestion,
        and then switches back to the default content.
        """
        self.logger.info(f"Attempting to select suggestion with text: '{text}'")

        # Always switch to the iframe before interacting with its elements
        self.switch_to_frame(DemoAutocompletePageLocators.categories_demo_iframe)

        try:
            suggestions = self.wait_for_all_elements_to_be_visible(DemoAutocompletePageLocators.autocomplete_suggestions_locator)
            for suggestion in suggestions:
                # Note: The text.strip() is crucial to handle any leading/trailing whitespace
                if suggestion.text.strip() == text:
                    # Use a more specific locator to avoid StaleElementReferenceException
                    self.element_click([("xpath", f"//div[text()='{text}']")])
                    self.logger.info(f"Clicked on suggestion: '{text}'")
                    return

            # If the loop finishes without finding the suggestion, log an error and raise an exception
            self.logger.warning(f"Suggestion '{text}' not found in the list.")
            raise NoSuchElementException(f"Suggestion '{text}' not found in the autocomplete list.")

        except StaleElementReferenceException:
            self.logger.info("StaleElementReferenceException occurred. Retrying to select suggestion.")
            # If the list is stale, try again
            self.select_suggestion_by_text(text)

        finally:
            # Crucial step: Always switch back to the default content
            # so other test methods don't fail because they are in the wrong frame.
            self.switch_to_default_content()


    def get_search_input_value(self):
        """
        Switches to the iframe, gets the value of the search input field,
        and then switches back to the default content.
        """
        # 1. Switch to the iframe
        self.switch_to_frame(DemoAutocompletePageLocators.categories_demo_iframe)

        try:
            # 2. Get the value of the search input field
            value = self.get_element_attribute(DemoAutocompletePageLocators.search_box_locator, "value")
            self.logger.info(f"Retrieved search input value: '{value}'")
            return value
        finally:
            # 3. Always switch back to the default content
            self.switch_to_default_content()


    def enter_text_combobox_search(self, text):
        """Types text into the autocomplete input field."""
        try:
            # Step 1: Switch to the iframe
            self.click_combobox_tab()
            self.switch_to_frame(DemoAutocompletePageLocators.combobox_demo_iframe)
            self.type_into_element(text, DemoAutocompletePageLocators.combobox_search_locator)
            # Step 2: Look for the element inside the iframe
            self.wait_for_element_to_be_visible(DemoAutocompletePageLocators.combobox_autosuggestions_locator, timeout=1)

            return True
        except:
            # If the element is not found within the timeout, return False
            return False
        finally:
            # Step 3: Always switch back to the default content
            self.switch_to_default_content()


   # --- New Methods for the Combobox Tab ---

    def get_combobox_suggestions(self):
        """
        Switches to the combobox iframe and returns a list of all visible suggestions.
        """
        self.switch_to_frame(DemoAutocompletePageLocators.combobox_demo_iframe)
        try:
            suggestions = self.wait_for_all_elements_to_be_visible(
                DemoAutocompletePageLocators.combobox_autosuggestions_locator
            )
            return suggestions
        except TimeoutException:
            self.logger.info("No combobox suggestions appeared within the timeout.")
            return []
        finally:
            self.switch_to_default_content()

    def select_combobox_suggestion_by_text(self, text: str):
        """
        Switches to the combobox iframe, finds a suggestion by text, clicks it,
        and switches back to the default content.
        """
        self.switch_to_frame(DemoAutocompletePageLocators.combobox_demo_iframe)
        try:
            # Create a dynamic locator for the specific suggestion
            suggestion_locator = self.get_dynamic_locator(
                DemoAutocompletePageLocators.combobox_suggestion_by_text,
                text
            )

            # Find and click the specific element with the given text
            self.element_click(suggestion_locator)
            self.logger.info(f"Successfully clicked on combobox suggestion: '{text}'")
            return True

        except (NoSuchElementException, TimeoutException):
            self.logger.warning(f"Combobox suggestion '{text}' not found.")
            return False
        finally:
            self.switch_to_default_content()

    def get_combobox_input_value(self):
        """
        Switches to the combobox iframe, retrieves the value of the input,
        and switches back to the default content.
        """
        self.switch_to_frame(DemoAutocompletePageLocators.combobox_demo_iframe)
        try:
            value = self.get_element_attribute(DemoAutocompletePageLocators.combobox_search_locator, "value")
            self.logger.info(f"Retrieved combobox input value: '{value}'")
            return value
        finally:
            self.switch_to_default_content()
