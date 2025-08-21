from pages.BasePage import BasePage
from pages.Header_Components import HeaderComponent
from locators.demosite_selectelements_page_locators import DemoSelectElementsPageLocators
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import pytest
import re

class DemoSelectElementsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.demoSelectElementsPageLocators = DemoSelectElementsPageLocators()

    def _click_tab(self, tab_locator: list):
        """
        Internal method to click on a tab.
        """
        self.logger.info(f"Clicking the tab with locator: {tab_locator}")
        self.element_click(tab_locator)
        time.sleep(2)

    def click_multiple_selection_tab(self):
        self._click_tab(DemoSelectElementsPageLocators.multiple_selection_tab_locator)

    def click_grid_selection_tab(self):
        self._click_tab(DemoSelectElementsPageLocators.grid_selection_tab_locator)

    def click_serialize_tab(self):
        self._click_tab(DemoSelectElementsPageLocators.serialize_tab_locator)


    # The corrected method to be placed within your page class.
    #Don't need this, the multiple selection will handle the single ones
    # def select_item_by_text(self, item_text):
    #     """
    #     Switches to the iframe, retrieves all selectable items, clicks the one that
    #     matches the given text, and then switches back to the default content.
    #
    #     Args:
    #         item_text (str): The exact text of the item to be selected.
    #     """
    #     self.logger.info(f"Attempting to select item with text: '{item_text}'")
    #
    #     try:
    #         # Step 1: Switch to the iframe before any interactions
    #         self.switch_to_frame(DemoSelectElementsPageLocators.multiple_selection_iframe_locator)
    #
    #         # Step 2: Get a list of all selectable list items
    #         selectable_items = self.get_elements(DemoSelectElementsPageLocators.multiple_selection_items_locator)
    #
    #         # Step 3: Loop through each element in the list to find a match
    #         found = False
    #         for item in selectable_items:
    #             # Check if the text of the current element matches the desired text.
    #             if item.text.strip() == item_text:
    #                 self.logger.info(f"Found item '{item_text}'. Clicking it.")
    #                 item.click()
    #                 found = True
    #                 break  # Exit the loop once the item is found and clicked.
    #
    #         # Step 4: Raise an exception if the item was not found
    #         if not found:
    #             self.logger.warning(f"Item with text '{item_text}' not found in the list.")
    #             raise NoSuchElementException(f"Item with text '{item_text}' not found.")
    #
    #     finally:
    #         # Step 5: Always switch back to the default content.
    #         # This is a crucial step to ensure the rest of your test continues correctly.
    #         self.switch_to_default_content()


    def select_multiple_items_by_text(self, item_texts_to_select: list):
        """
        Switches to the iframe, selects a list of items using Ctrl+Click,
        and then switches back to the default content.

        Args:
            item_texts_to_select (list): A list of strings, where each string
                                         is the exact text of an item to be selected.
        """

        self.switch_to_frame(DemoSelectElementsPageLocators.multiple_selection_iframe_locator)

        try:
            # Step 1: Switch to the iframe before any interactions

            self.wait_for_element_to_be_visible(DemoSelectElementsPageLocators.multiple_selection_items_locator)

            self.multiselect_items_by_text(DemoSelectElementsPageLocators.multiple_selection_items_locator, item_texts=item_texts_to_select)

            self.logger.info(f"Successfully performed multiselect on all requested items.")

        except Exception as e:
            # Log the error, but let the `finally` block handle the cleanup.
            self.logger.error(f"Failed to perform multiselect: {e}")
            raise # Re-raise the exception to fail the test.

        finally:
            # Step 3: Always switch back to the default content, regardless of what happened.
            self.switch_to_default_content()
            self.logger.info("Switched back to default content.")


    def verify_selected_items(self, expected_selected_texts: list) -> bool:
        """
        Verifies that a specific list of items are selected, and no others.

        This method first checks that all the expected items have the 'ui-selected' class.
        Then, it checks that only these items are selected by ensuring the total
        count of selected items matches the expected count.

        Args:
            expected_selected_texts (list): A list of strings corresponding to the
                                            items that should be selected.

        Returns:
            bool: True if the verification passes, False otherwise.
        """
        print("Starting verify")
        self.logger.info("Switching to iframe to verify selected items.")
        self.switch_to_frame(DemoSelectElementsPageLocators.multiple_selection_iframe_locator)

        try:

            selected_elements = self.get_elements(DemoSelectElementsPageLocators.multiple_selected_items_locator)

            # Check if the number of selected elements matches the expected number.
            if len(selected_elements) != len(expected_selected_texts):
                self.logger.error(f"Mismatch in selected item count. Expected {len(expected_selected_texts)}, but found {len(selected_elements)}.")
                return False

            # Check if each selected element's text is in our expected list.
            for element in selected_elements:
                if element.text not in expected_selected_texts:
                    self.logger.error(f"Unexpected item '{element.text}' found in the selected list.")
                    return False

            self.logger.info("All selected items verified successfully.")
            return True
        except NoSuchElementException as e:
            self.logger.error(f"Verification failed: {e}")
            return False
        finally:
            self.switch_to_default_content()
            self.logger.info("Switched back to default content after verification.")


    def select_items_with_drag_and_drop(self, start_text: str, end_text: str):
        """
        Switches to the iframe and performs a drag-and-drop to select
        a range of items, then closes the native Windows menu.

        Args:
            start_text (str): The text of the first item to select.
            end_text (str): The text of the last item to select.
        """
        self.logger.info("Starting drag-and-drop multiselect process...")

        # Step 1: Switch to the iframe.
        self.switch_to_frame(DemoSelectElementsPageLocators.multiple_selection_iframe_locator)
        self.logger.info("Switched to multiple selection iframe.")

        try:
            # Step 2: Find the start and end elements for the drag action.
            self.logger.info(f"Finding start element with text: {start_text}")
            start_element = self.find_element_by_text(
                DemoSelectElementsPageLocators.multiple_selection_items_locator,
                start_text
            )

            self.logger.info(f"Finding end element with text: {end_text}")
            end_element = self.find_element_by_text(
                DemoSelectElementsPageLocators.multiple_selection_items_locator,
                end_text
            )

            # Step 3: Perform the drag-and-drop action using ActionChains.
            self.logger.info("Performing drag-and-drop from start to end element.")
            self.click_and_drag_elements(start_element,end_element)

            self.logger.info(f"Successfully performed drag-and-drop multiselect from '{start_text}' to '{end_text}'.")

        except Exception as e:
            self.logger.error(f"Failed to perform drag-and-drop multiselect: {e}")
            raise # Re-raise the exception.

        finally:
            # Step 5: Always switch back to the default content.
            self.switch_to_default_content()
            self.logger.info("Switched back to default content.")

    # Grid Selection Items
    # Note - we can get rid of some of the repeated methods by feeding in the locators to a generic method

    def select_multiple_grid_items_by_text(self, item_texts_to_select: list):
        """
        Switches to the iframe, selects a list of items using Ctrl+Click,
        and then switches back to the default content.

        Args:
            item_texts_to_select (list): A list of strings, where each string
                                         is the exact text of an item to be selected.
        """

        self.switch_to_frame(DemoSelectElementsPageLocators.grid_selection_iframe_locator)

        try:
            # Step 1: Switch to the iframe before any interactions

            self.multiselect_items_by_text(DemoSelectElementsPageLocators.grid_selection_items_locator, item_texts=item_texts_to_select)

            self.logger.info(f"Successfully performed multiselect on all requested items.")

        except Exception as e:
            # Log the error, but let the `finally` block handle the cleanup.
            self.logger.error(f"Failed to perform multiselect: {e}")
            raise # Re-raise the exception to fail the test.

        finally:
            # Step 3: Always switch back to the default content, regardless of what happened.
            self.switch_to_default_content()
            self.logger.info("Switched back to default content.")


    def verify_grid_selected_items(self, expected_selected_texts: list) -> bool:
        """
        Verifies that a specific list of items are selected, and no others.

        This method first checks that all the expected items have the 'ui-selected' class.
        Then, it checks that only these items are selected by ensuring the total
        count of selected items matches the expected count.

        Args:
            expected_selected_texts (list): A list of strings corresponding to the
                                            items that should be selected.

        Returns:
            bool: True if the verification passes, False otherwise.
        """
        print("Starting verify")
        self.logger.info("Switching to iframe to verify selected items.")
        self.switch_to_frame(DemoSelectElementsPageLocators.grid_selection_iframe_locator)

        try:

            selected_elements = self.get_elements(DemoSelectElementsPageLocators.grid_selected_items_locator)

            # Check if the number of selected elements matches the expected number.
            if len(selected_elements) != len(expected_selected_texts):
                self.logger.error(f"Mismatch in selected item count. Expected {len(expected_selected_texts)}, but found {len(selected_elements)}.")
                return False

            # Check if each selected element's text is in our expected list.
            for element in selected_elements:
                if element.text not in expected_selected_texts:
                    self.logger.error(f"Unexpected item '{element.text}' found in the selected list.")
                    return False

            self.logger.info("All selected items verified successfully.")
            return True
        except NoSuchElementException as e:
            self.logger.error(f"Verification failed: {e}")
            return False
        finally:
            self.switch_to_default_content()
            self.logger.info("Switched back to default content after verification.")


    def select_grid_item_by_text(self, item_text):
        """
        Switches to the iframe, retrieves all selectable items, clicks the one that
        matches the given text, and then switches back to the default content.

        Args:
            item_text (str): The exact text of the item to be selected.
        """
        self.logger.info(f"Attempting to select item with text: '{item_text}'")

        try:
            # Step 1: Switch to the iframe before any interactions
            self.switch_to_frame(DemoSelectElementsPageLocators.grid_selection_iframe_locator)

            # Step 2: Get a list of all selectable list items
            selectable_items = self.get_elements(DemoSelectElementsPageLocators.grid_selection_items_locator)

            # Step 3: Loop through each element in the list to find a match
            found = False
            for item in selectable_items:
                # Check if the text of the current element matches the desired text.
                if item.text.strip() == item_text:
                    self.logger.info(f"Found item '{item_text}'. Clicking it.")
                    item.click()
                    found = True
                    break  # Exit the loop once the item is found and clicked.

            # Step 4: Raise an exception if the item was not found
            if not found:
                self.logger.warning(f"Item with text '{item_text}' not found in the list.")
                raise NoSuchElementException(f"Item with text '{item_text}' not found.")

        finally:
            # Step 5: Always switch back to the default content.
            # This is a crucial step to ensure the rest of your test continues correctly.
            self.switch_to_default_content()

    #Serialize Methods
    #Same thing, we can get rid of some of these after we get them going by making generic methods


    def select_multiple_serialize_items_by_text(self, item_texts_to_select: list):
        """
        Switches to the iframe, selects a list of items using Ctrl+Click,
        and then switches back to the default content.

        Args:
            item_texts_to_select (list): A list of strings, where each string
                                         is the exact text of an item to be selected.
        """

        self.switch_to_frame(DemoSelectElementsPageLocators.serialize_iframe_locator)

        try:
            # Step 1: Switch to the iframe before any interactions

            self.multiselect_items_by_text(DemoSelectElementsPageLocators.serialize_selection_items_locator, item_texts=item_texts_to_select)

            self.logger.info(f"Successfully performed multiselect on all requested items.")

        except Exception as e:
            # Log the error, but let the `finally` block handle the cleanup.
            self.logger.error(f"Failed to perform multiselect: {e}")
            raise # Re-raise the exception to fail the test.

        finally:
            # Step 3: Always switch back to the default content, regardless of what happened.
            self.switch_to_default_content()
            self.logger.info("Switched back to default content.")


    def verify_selected_serialize_items(self, expected_selected_texts: list) -> bool:
        """
        Verifies that a specific list of items are selected, and no others.

        This method first checks that all the expected items have the 'ui-selected' class.
        Then, it checks that only these items are selected by ensuring the total
        count of selected items matches the expected count.

        Args:
            expected_selected_texts (list): A list of strings corresponding to the
                                            items that should be selected.

        Returns:
            bool: True if the verification passes, False otherwise.
        """
        print("Starting verify")
        self.logger.info("Switching to iframe to verify selected items.")
        self.switch_to_frame(DemoSelectElementsPageLocators.serialize_iframe_locator)

        try:

            selected_elements = self.get_elements(DemoSelectElementsPageLocators.serialize_selected_items_locator)

            # Check if the number of selected elements matches the expected number.
            if len(selected_elements) != len(expected_selected_texts):
                self.logger.error(f"Mismatch in selected item count. Expected {len(expected_selected_texts)}, but found {len(selected_elements)}.")
                return False

            # Check if each selected element's text is in our expected list.
            for element in selected_elements:
                if element.text not in expected_selected_texts:
                    self.logger.error(f"Unexpected item '{element.text}' found in the selected list.")
                    return False

            self.logger.info("All selected items verified successfully.")
            return True
        except NoSuchElementException as e:
            self.logger.error(f"Verification failed: {e}")
            return False
        finally:
            self.switch_to_default_content()
            self.logger.info("Switched back to default content after verification.")


    def select_serialize_items_with_drag_and_drop(self, start_text: str, end_text: str):
        """
        Switches to the iframe and performs a drag-and-drop to select
        a range of items, then closes the native Windows menu.

        Args:
            start_text (str): The text of the first item to select.
            end_text (str): The text of the last item to select.
        """
        self.logger.info("Starting drag-and-drop multiselect process...")

        # Step 1: Switch to the iframe.
        self.switch_to_frame(DemoSelectElementsPageLocators.serialize_iframe_locator)
        self.logger.info("Switched to multiple selection iframe.")

        try:
            # Step 2: Find the start and end elements for the drag action.
            self.logger.info(f"Finding start element with text: {start_text}")
            start_element = self.find_element_by_text(
                DemoSelectElementsPageLocators.serialize_selection_items_locator,
                start_text
            )

            self.logger.info(f"Finding end element with text: {end_text}")
            end_element = self.find_element_by_text(
                DemoSelectElementsPageLocators.serialize_selection_items_locator,
                end_text
            )

            # Step 3: Perform the drag-and-drop action using ActionChains.
            self.logger.info("Performing drag-and-drop from start to end element.")
            self.click_and_drag_elements(start_element,end_element)

            self.logger.info(f"Successfully performed drag-and-drop multiselect from '{start_text}' to '{end_text}'.")

        except Exception as e:
            self.logger.error(f"Failed to perform drag-and-drop multiselect: {e}")
            raise # Re-raise the exception.

        finally:
            # Step 5: Always switch back to the default content.
            self.switch_to_default_content()
            self.logger.info("Switched back to default content.")

    def verify_serialize_selection_text(self, expected_text: str):
        """
        Waits for and verifies that the selection feedback text matches
        the expected value.

        Args:
            expected_text (str): The exact text string to verify.
                                 e.g., "none" or " #4".
        """
        self.switch_to_frame(DemoSelectElementsPageLocators.serialize_iframe_locator)
        self.logger.info("Switched to multiple selection iframe.")
        self.logger.info(f"Verifying selection result text is '{expected_text}'.")
        try:

            self.find_element_by_text(DemoSelectElementsPageLocators.serialize_selected_text_locator,
                expected_text)
            self.logger.info("Successfully verified text.")
        except Exception as e:
            self.logger.error(f"Text verification failed. Expected '{expected_text}', "
                              f"but it was not found. Error: {e}")
            raise AssertionError(f"Selection feedback text did not match '{expected_text}'.")

        finally:
            # Step 5: Always switch back to the default content.
            self.switch_to_default_content()
            self.logger.info("Switched back to default content.")
