from pages.BasePage import BasePage
from pages.Header_Components import HeaderComponent
from locators.demosite_sorting_page_locators import DemoSortingPageLocators
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
import time
import pytest
import re

class DemoSortingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.DemoSortingPageLocators = DemoSortingPageLocators()

        # Create a dictionary to easily get the locator based on the list ID
        self.list_locators = {
            "sortable1": DemoSortingPageLocators.sortable1_items_locator,
            "sortable2": DemoSortingPageLocators.sortable2_items_locator,
        }

    def _click_tab(self, tab_locator: list):
        """
        Internal method to click on a tab.
        """
        self.logger.info(f"Clicking the tab with locator: {tab_locator}")
        self.element_click(tab_locator)
        time.sleep(2)

    def click_portlets_tab(self):
        self._click_tab(DemoSortingPageLocators.click_portlets_tab)

    def click_multiple_lists_tab(self):
        self._click_tab(DemoSortingPageLocators.click_multiple_lists_tab)

    def click_simple_list_tab(self):
        self._click_tab(DemoSortingPageLocators.click_simple_list_tab)

    def click_grid_sorting_tab(self):
        self._click_tab(DemoSortingPageLocators.click_grid_sorting_tab)



    def portlets_drag_and_drop_to_sort(self, start_text: str, end_text: str):
        """
        Switches to the iframe and performs a drag-and-drop to select
        a range of items, then closes the native Windows menu.

        Args:
            start_text (str): The text of the first item to select.
            end_text (str): The text of the last item to select.
        """
        self.logger.info("Starting drag-and-drop multiselect process...")

        # Step 1: Switch to the iframe.
        self.switch_to_frame(DemoSortingPageLocators.portlets_iframe_locator)
        self.logger.info("Switched to multiple selection iframe.")

        try:
            # Step 2: Find the start and end elements for the drag action.
            self.logger.info(f"Finding start element with text: {start_text}")
            start_element = self.find_element_by_text(
                DemoSortingPageLocators.all_portlet_headers_locator,
                start_text
            )

            self.logger.info(f"Finding end element with text: {end_text}")
            end_element = self.find_element_by_text(
                DemoSortingPageLocators.all_portlet_headers_locator,
                end_text
            )

            # Step 3: Perform the drag-and-drop action using ActionChains.
            self.logger.info("Performing drag-and-drop from start to end element.")
            self.click_and_drag_elements(start_element,end_element)

            self.logger.info(f"Successfully performed drag-and-drop multiselect from '{start_text}' to '{end_text}'.")

        except Exception as e:
            self.logger.error(f"Failed to perform drag-and-drop: {e}")
            raise # Re-raise the exception.

        finally:
            # Step 5: Always switch back to the default content.
            self.switch_to_default_content()
            self.logger.info("Switched back to default content.")

    def multiple_lists_drag_and_drop_to_sort(self, start_text: str, start_list_id: str, end_text: str, end_list_id: str):
        """
        Switches to the iframe and performs a drag-and-drop to sort items
        between two different lists, using list IDs to ensure specificity.

        Args:
            start_text (str): The text of the item to drag.
            start_list_id (str): The ID of the list where the item to drag is located (e.g., 'sortable1').
            end_text (str): The text of the item to drop onto.
            end_list_id (str): The ID of the list where the drop target is located (e.g., 'sortable2').
        """



        self.logger.info("Starting drag-and-drop sort process between two lists...")

        # Step 1: Switch to the iframe.
        self.switch_to_frame(DemoSortingPageLocators.multiple_lists_iframe_locator)
        self.logger.info("Switched to multiple lists iframe.")

        try:
            # Step 2: Use the list IDs to retrieve the correct locator from the dictionary.
            start_element_locator = self.list_locators.get(start_list_id)
            end_element_locator = self.list_locators.get(end_list_id)

            # Raise an error if an invalid list ID is provided
            if not start_element_locator or not end_element_locator:
                raise ValueError("Invalid list ID provided. Must be 'sortable1' or 'sortable2'.")

            self.logger.info(f"Finding start element '{start_text}' in list '{start_list_id}'")
            start_element = self.find_element_by_text(start_element_locator, start_text)

            self.logger.info(f"Finding end element '{end_text}' in list '{end_list_id}'")
            end_element = self.find_element_by_text(end_element_locator, end_text)

            # Step 4: Perform the drag-and-drop action using the generic method.
            self.logger.info("Performing drag-and-drop from start to end element.")
            self.click_and_drag_elements(start_element, end_element)

            self.logger.info(f"Successfully performed drag-and-drop from '{start_text}' (in '{start_list_id}') to '{end_text}' (in '{end_list_id}').")

        except (NoSuchElementException, TimeoutException, StaleElementReferenceException) as e:
            self.logger.error(f"Failed to find element during drag-and-drop: {e}")
            raise
        except Exception as e:
            self.logger.error(f"Failed to perform drag-and-drop: {e}")
            raise
        finally:
            # Step 5: Always switch back to the default content.
            self.switch_to_default_content()
            self.logger.info("Switched back to default content.")

    def verify_multiple_lists_order(self, list_id: str, expected_order: list):
        """
        Switches to the iframe, gets the current list order, and asserts it matches
        the expected order.

        Args:
            list_id (str): The ID of the list to verify (e.g., 'sortable1').
            expected_order (list): A list of strings representing the expected order of items.
        """
        self.logger.info(f"Starting verification of list '{list_id}'.")
        print(f"Starting verification of list '{list_id}'.")
        # Step 1: Switch to the iframe.
        self.switch_to_frame(DemoSortingPageLocators.multiple_lists_iframe_locator)
        self.logger.info("Switched to multiple lists iframe.")

        try:
            # Step 2: Get the locator for all items in the specified list.
            items_locator = self.DemoSortingPageLocators.get_list_items_locator(list_id)

            # Step 3: Find all the elements and extract their text.
            list_elements = self.get_elements(items_locator)
            current_order = [element.text for element in list_elements]

            # Step 4: Assert that the current order matches the expected order.
            self.logger.info(f"Current order in list '{list_id}': {current_order}")
            self.logger.info(f"Expected order for list '{list_id}': {expected_order}")

            assert current_order == expected_order, \
                f"List order verification failed! Expected: {expected_order}, but got: {current_order}"

            self.logger.info(f"List '{list_id}' order successfully verified.")

        except (NoSuchElementException, TimeoutException) as e:
            self.logger.error(f"Failed to verify list order: {e}")
            raise
        finally:
            # Step 5: Always switch back to the default content.
            self.switch_to_default_content()
            self.logger.info("Switched back to default content.")



    def simple_list_drag_and_drop_to_sort(self, start_text: str, end_text: str):
        """
        Switches to the iframe and performs a drag-and-drop to select
        a range of items, then closes the native Windows menu.

        Args:
            start_text (str): The text of the first item to select.
            end_text (str): The text of the last item to select.
        """
        self.logger.info("Starting drag-and-drop multiselect process...")

        # Step 1: Switch to the iframe.
        self.switch_to_frame(DemoSortingPageLocators.simple_list_iframe_locator)
        self.logger.info("Switched to multiple selection iframe.")

        try:
            # Step 2: Find the start and end elements for the drag action.
            self.logger.info(f"Finding start element with text: {start_text}")
            start_element = self.find_element_by_text(
                DemoSortingPageLocators.simple_list_items_locator,
                start_text
            )

            start_handle = self.get_child_element(start_element, DemoSortingPageLocators.simple_list_item_handle_locator)

            self.logger.info(f"Finding end element with text: {end_text}")
            end_element = self.find_element_by_text(
                DemoSortingPageLocators.simple_list_items_locator,
                end_text
            )

            end_handle = self.get_child_element(end_element, DemoSortingPageLocators.simple_list_item_handle_locator)

            # Step 3: Perform the drag-and-drop action using ActionChains.
            self.logger.info("Performing drag-and-drop from start to end element.")
            self.click_and_drag_elements(start_handle,end_handle)

            self.logger.info(f"Successfully performed drag-and-drop multiselect from '{start_text}' to '{end_text}'.")

        except Exception as e:
            self.logger.error(f"Failed to perform drag-and-drop: {e}")
            raise # Re-raise the exception.

        finally:
            # Step 5: Always switch back to the default content.
            self.switch_to_default_content()
            self.logger.info("Switched back to default content.")




    def verify_simple_list_order(self, expected_order: list):
        """
        Verifies the order of the single list on the "Simple List" tab.

        Args:
            expected_order (list): A list of strings representing the expected order of items.
        """

        self.logger.info("Starting verification of the simple list.")
        self.switch_to_frame(DemoSortingPageLocators.simple_list_iframe_locator)
        self.logger.info("Switched to simple list iframe.")

        try:
            # Find all the list item elements
            list_elements = self.get_elements(DemoSortingPageLocators.simple_list_items_locator)

            # Extract the text from each element to create a list of the current order
            current_order = [element.text for element in list_elements]

            self.logger.info(f"Current order in list: {current_order}")
            self.logger.info(f"Expected order for list: {expected_order}")

            # Assert that the current order matches the expected order
            assert current_order == expected_order, \
                f"Simple list order verification failed! Expected: {expected_order}, but got: {current_order}"

            self.logger.info("Simple list order successfully verified.")

        except (NoSuchElementException, TimeoutException) as e:
            self.logger.error(f"Failed to verify simple list order: {e}")
            raise
        finally:
            self.switch_to_default_content()
            self.logger.info("Switched back to default content.")

    def grid_sorting_drag_and_drop_to_sort(self, start_text: str, end_text: str):
        """
        Switches to the iframe and performs a drag-and-drop to select
        a range of items, then closes the native Windows menu.

        Args:
            start_text (str): The text of the first item to select.
            end_text (str): The text of the last item to select.
        """
        self.logger.info("Starting drag-and-drop multiselect process...")

        # Step 1: Switch to the iframe.
        self.switch_to_frame(DemoSortingPageLocators.grid_sorting_iframe_locator)
        self.logger.info("Switched to multiple selection iframe.")

        try:
            # Step 2: Find the start and end elements for the drag action.
            self.logger.info(f"Finding start element with text: {start_text}")
            start_element = self.find_element_by_text(
                DemoSortingPageLocators.grid_sorting_items_locator,
                start_text
            )

            self.logger.info(f"Finding end element with text: {end_text}")
            end_element = self.find_element_by_text(
                DemoSortingPageLocators.grid_sorting_items_locator,
                end_text
            )

            # Step 3: Perform the drag-and-drop action using ActionChains.
            self.logger.info("Performing drag-and-drop from start to end element.")
            self.click_and_drag_elements(start_element,end_element)

            self.logger.info(f"Successfully performed drag-and-drop multiselect from '{start_text}' to '{end_text}'.")

        except Exception as e:
            self.logger.error(f"Failed to perform drag-and-drop: {e}")
            raise # Re-raise the exception.

        finally:
            # Step 5: Always switch back to the default content.
            self.switch_to_default_content()
            self.logger.info("Switched back to default content.")




    def verify_grid_reorder_list_order(self, expected_order: list):
        """
        Verifies the order of the single list on the "Simple List" tab.

        Args:
            expected_order (list): A list of strings representing the expected order of items.
        """

        self.logger.info("Starting verification of the simple list.")
        self.switch_to_frame(DemoSortingPageLocators.grid_sorting_iframe_locator)
        self.logger.info("Switched to simple list iframe.")

        try:
            # Find all the list item elements
            list_elements = self.get_elements(DemoSortingPageLocators.grid_sorting_items_locator)

            # Extract the text from each element to create a list of the current order
            current_order = [element.text for element in list_elements]

            self.logger.info(f"Current order in list: {current_order}")
            self.logger.info(f"Expected order for list: {expected_order}")

            # Assert that the current order matches the expected order
            assert current_order == expected_order, \
                f"Simple list order verification failed! Expected: {expected_order}, but got: {current_order}"

            self.logger.info("Simple list order successfully verified.")

        except (NoSuchElementException, TimeoutException) as e:
            self.logger.error(f"Failed to verify simple list order: {e}")
            raise
        finally:
            self.switch_to_default_content()
            self.logger.info("Switched back to default content.")
