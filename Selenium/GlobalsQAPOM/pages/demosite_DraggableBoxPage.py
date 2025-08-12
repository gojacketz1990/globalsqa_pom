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

    def click_simpledrag_tab(self):
        self._click_tab(DemoDraggableBoxPageLocators.simple_drag_tab_locator)

    def click_checkevents_tab(self):
        self._click_tab(DemoDraggableBoxPageLocators.check_events_tab_locator)

    def click_handle_tab(self):
        self._click_tab(DemoDraggableBoxPageLocators.handle_tab_locator)

    def click_constraints_tab(self):
        self._click_tab(DemoDraggableBoxPageLocators.constraints_tab_locator)

    def drag_box_by_offset(self, x_offset: int, y_offset: int):
        #Starts at:
        """
        Drags the draggable box by a specified offset (x, y) relative to its current position.

        Args:
            x_offset (int): The horizontal distance to drag (positive for right, negative for left).
            y_offset (int): The vertical distance to drag (positive for down, negative for up).
        """
        self.switch_to_frame(DemoDraggableBoxPageLocators.simple_drag_iframe)
        try:
            self.logger.info(f"Attempting to drag box by offset: ({x_offset}, {y_offset}).")
            draggable_element = self.get_element(DemoDraggableBoxPageLocators.simple_drag_box_locator)

            # Using ActionChains to perform the drag
            self.drag_element_by_offset(draggable_element, x_offset,y_offset)

            self.logger.info("Drag operation completed.")
            # A small pause might be needed depending on the UI responsiveness
            time.sleep(0.5)
        except Exception as e:
            self.logger.error(f"Failed to drag box by offset: {e}")
            raise
        finally:
            self.switch_to_default_content()

    def get_draggable_box_position(self) -> dict:
        """
        Retrieves the current x and y coordinates of the draggable box.

        Returns:
            dict: A dictionary with 'x' and 'y' keys representing the element's position.
        """
        self.switch_to_frame(DemoDraggableBoxPageLocators.simple_drag_iframe)
        try:
            draggable_element = self.get_element(DemoDraggableBoxPageLocators.simple_drag_box_locator)
            location = draggable_element.location
            self.logger.info(f"Draggable box position: X={location['x']}, Y={location['y']}")
            return location
        finally:
            self.switch_to_default_content()
