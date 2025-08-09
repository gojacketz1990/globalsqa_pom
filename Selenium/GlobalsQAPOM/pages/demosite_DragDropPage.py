from pages.BasePage import BasePage
from pages.Header_Components import HeaderComponent
from locators.demosite_drag_drop_page_locators import DemoDragDropPageLocators
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
import time
import datetime
import pytest
import re

class DemoDragDropPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.demoDragDropPageLocators = DemoDragDropPageLocators()


    def _click_tab(self, tab_locator: list):
        """
        Internal method to click on a tab.
        """
        self.logger.info(f"Clicking the tab with locator: {tab_locator}")
        self.element_click(tab_locator)
        time.sleep(2)


    def click_photo_manager_tab(self):
        self._click_tab(DemoDragDropPageLocators.click_photo_manager_tab_locator)

    def click_accepted_elements_tab(self):
        self._click_tab(DemoDragDropPageLocators.click_accepted_elements_tab_locator)

    def click_propagation_tab(self):
        self._click_tab(DemoDragDropPageLocators.click_propagation_tab_locator)

    def is_item_in_trash(self, item_name: str) -> bool:
        """
        Checks if a specific gallery item is in the trash container.

        Args:
            item_name (str): The name of the item to check for (e.g., 'High Tatras').

        Returns:
            bool: True if the item is found in the trash, False otherwise.
        """
        self.switch_to_frame(DemoDragDropPageLocators.photo_manager_demo_iframe)
        trash_item_locator = self.get_dynamic_locator(
            DemoDragDropPageLocators.trash_item_by_name,
            item_name
        )

        try:
            # Use get_element to check for existence without needing it to be clickable
            self.get_element(trash_item_locator)
            self.logger.info(f"Item '{item_name}' found in the trash.")
            return True
        except NoSuchElementException:
            self.logger.warning(f"Item '{item_name}' was not found in the trash.")
            return False
        finally:
            # Step 5: Always switch back to the default content.
            self.switch_to_default_content()
            self.logger.info("Switched back to default content.")



    def is_item_in_gallery(self, item_name: str) -> bool:
        """
        Verifies if a specific gallery item is present in the original gallery.
        """
        self.switch_to_frame(DemoDragDropPageLocators.photo_manager_demo_iframe)
        gallery_item_locator = self.get_dynamic_locator(DemoDragDropPageLocators.gallery_item_by_name, item_name)

        try:
            # Use get_element to check for the element's existence
            self.get_element(gallery_item_locator)
            self.logger.warning(f"Item '{item_name}' is still in the gallery.")
            return True
        except NoSuchElementException:
            self.logger.info(f"Item '{item_name}' is no longer in the gallery.")
            return False
        finally:
            # Step 5: Always switch back to the default content.
            self.switch_to_default_content()
            self.logger.info("Switched back to default content.")

    def get_gallery_item_by_name(self, item_name: str):
        """
        Retrieves a specific gallery list item (<li>) by its header text.

        Args:
            item_name (str): The text of the <h5> header to search for (e.g., 'High Tatras').

        Returns:
            WebElement: The WebElement corresponding to the gallery item.
        """
        # Create a dynamic locator for the specific item

        self.switch_to_frame(DemoDragDropPageLocators.photo_manager_demo_iframe)
        item_locator = self.get_dynamic_locator(DemoDragDropPageLocators.gallery_item_by_name, item_name)

        try:
            # Return the element using the dynamic locator
            return self.get_element(item_locator)
        except NoSuchElementException:
            self.logger.error(f"Gallery item with name '{item_name}' not found.")
            raise
        finally:
            # Step 5: Always switch back to the default content.
            self.switch_to_default_content()
            self.logger.info("Switched back to default content.")




    def select_items_with_drag_and_drop(self, start_text: str):
        """
        Switches to the iframe and performs a drag-and-drop to select
        a range of items, then closes the native Windows menu.

        Args:
            start_text (str): The text of the first item to select.
            end_text (str): The text of the last item to select.
        """
        self.logger.info("Starting drag-and-drop multiselect process...")

        # Step 1: Switch to the iframe.
        self.switch_to_frame(DemoDragDropPageLocators.photo_manager_demo_iframe)

        try:
            # Step 2: Find the start and end elements for the drag action.
            self.logger.info(f"Finding start element with text: {start_text}")
            start_element = self.get_gallery_item_by_name(start_text)


            end_element = self.get_element(DemoDragDropPageLocators.trash_locator)


            # Step 3: Perform the drag-and-drop action using ActionChains.
            self.logger.info("Performing drag-and-drop from start to end element.")
            self.click_and_drag_elements(start_element,end_element)
        except Exception as e:
            self.logger.error(f"Failed to perform drag-and-drop multiselect: {e}")
            raise # Re-raise the exception.

        finally:
            # Step 5: Always switch back to the default content.
            self.switch_to_default_content()
            self.logger.info("Switched back to default content.")



    def drag_and_drop_invalid_item_to_trash(self) -> None:
        """
        Performs a drag-and-drop of the non-valid item to the droppable area.
        """
        self.switch_to_frame(DemoDragDropPageLocators.accepted_elements_demo_iframe)
        try:
            draggable = self.get_element(DemoDragDropPageLocators.draggable_not_droppable_locator)
            droppable = self.get_element(DemoDragDropPageLocators.droppable_area_locator)

            self.logger.info("Attempting to drag non-valid item to droppable area.")
            self.click_and_drag_elements(draggable,droppable)

            self.logger.info("Drag-and-drop action completed.")
        finally:
            self.switch_to_default_content()

    def drag_and_drop_valid_item_to_trash(self) -> None:
        """
        Performs a drag-and-drop of the non-valid item to the droppable area.
        """
        self.switch_to_frame(DemoDragDropPageLocators.accepted_elements_demo_iframe)
        try:
            draggable = self.get_element(DemoDragDropPageLocators.draggable_and_droppable_locator)
            droppable = self.get_element(DemoDragDropPageLocators.droppable_area_locator)

            self.logger.info("Attempting to drag non-valid item to droppable area.")
            self.click_and_drag_elements(draggable,droppable)

            self.logger.info("Drag-and-drop action completed.")
        finally:
            self.switch_to_default_content()

    def is_droppable_item_unchanged(self) -> bool:
        """
        Verifies that the droppable area's class has not changed after a drop.
        Returns:
            bool: True if the droppable item remains unchanged, False otherwise.
        """
        self.switch_to_frame(DemoDragDropPageLocators.accepted_elements_demo_iframe)
        try:
            droppable_element = self.get_element(DemoDragDropPageLocators.droppable_area_locator)
            current_class = droppable_element.get_attribute("class")

            # Check if the class contains a "changed" state
            return "ui-droppable-hover" not in current_class and "ui-state-highlight" not in current_class
        finally:
            self.switch_to_default_content()

    def get_droppable_text(self) -> str:
        """
        Retrieves the text of the droppable area.
        """
        self.switch_to_frame(DemoDragDropPageLocators.accepted_elements_demo_iframe)
        try:
            return self.retrieve_element_text(DemoDragDropPageLocators.droppable_area_locator)
        finally:
            self.switch_to_default_content()

    def drag_and_drop_valid_item(self) -> None:
        """
        Performs a drag-and-drop of the non-valid item to the droppable area.
        """
        self.switch_to_frame(DemoDragDropPageLocators.accepted_elements_demo_iframe)
        try:
            draggable = self.get_element(DemoDragDropPageLocators.draggable_and_droppable_locator)
            droppable = self.get_element(DemoDragDropPageLocators.droppable_area_locator)

            self.logger.info("Attempting to drag non-valid item to droppable area.")
            self.click_and_drag_elements(draggable,droppable)

            self.logger.info("Drag-and-drop action completed.")
        finally:
            self.switch_to_default_content()
