from pages.BasePage import BasePage
from pages.Header_Components import HeaderComponent
from locators.demosite_date_picker_page_locators import DemoDatePickerPageLocators
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
import time
import datetime
import pytest
import re

class DemoDatePickerPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.demoDatePickerPageLocators = DemoDatePickerPageLocators()


    def _click_tab(self, tab_locator: list):
        """
        Internal method to click on a tab.
        """
        self.logger.info(f"Clicking the tab with locator: {tab_locator}")
        self.element_click(tab_locator)
        time.sleep(2)

    def click_dropdown_datepicker_tab(self):
        self._click_tab(DemoDatePickerPageLocators.dropdown_datepicker_tab_locator)

    def click_date_picker_tab(self):
        self._click_tab(DemoDatePickerPageLocators.simple_date_picker_tab_locator)

    def click_icon_trigger_tab(self):
        self._click_tab(DemoDatePickerPageLocators.icon_trigger_tab_locator)


    def click_simple_date_textbox(self):


        self.switch_to_frame(DemoDatePickerPageLocators.simple_date_picker_demo_iframe)
        try:
            self.element_click(DemoDatePickerPageLocators.date_field_locator)

        finally:
            self.switch_to_default_content() # Always switch back

    def click_dropdown_datepicker_date_textbox(self):


        self.switch_to_frame(DemoDatePickerPageLocators.dropdown_datepicker_demo_iframe)
        try:
            self.element_click(DemoDatePickerPageLocators.date_field_locator)

        finally:
            self.switch_to_default_content() # Always switch back


    def select_simple_date(self, target_date_str: str):
        """
        Selects a date from the jQuery UI date picker.
        Args:
            target_date_str: The date to select in "YYYY-MM-DD" format.
        """
        self.switch_to_frame(DemoDatePickerPageLocators.simple_date_picker_demo_iframe)
        try:
            self.logger.info(f"Attempting to select date: {target_date_str}")

            # 1. Parse the target date string
            target_date = datetime.datetime.strptime(target_date_str, "%m/%d/%Y")

            # 2. Click the input field to open the date picker
            self.element_click(DemoDatePickerPageLocators.date_field_locator)

            # 3. Navigate to the correct month and year
            while True:
                current_month = self.retrieve_element_text(DemoDatePickerPageLocators.datepicker_month)
                current_year = self.retrieve_element_text(DemoDatePickerPageLocators.datepicker_year)

                # Check if we are in the correct month and year
                if current_month == target_date.strftime("%B") and current_year == str(target_date.year):
                    self.logger.info(f"Now in the correct month/year: {current_month} {current_year}")
                    break

                # If not, navigate forward or backward
                current_date = datetime.datetime.strptime(f"{current_year}-{current_month}", "%Y-%B")
                if target_date > current_date:
                    self.logger.info(f"Moving to next month...")
                    self.element_click(DemoDatePickerPageLocators.datepicker_next_button)
                else:
                    self.logger.info(f"Moving to previous month...")
                    self.element_click(DemoDatePickerPageLocators.datepicker_prev_button)
                time.sleep(1)
            # 4. Select the day
            # Use a dynamic locator to find the day link by its text (the day number)
            day_locator = self.get_dynamic_locator(
                DemoDatePickerPageLocators.datepicker_day_by_number,
                str(target_date.day)
            )
            self.element_click(day_locator)
            self.logger.info(f"Successfully selected day: {target_date.day}")

        except (NoSuchElementException, TimeoutException) as e:
            self.logger.error(f"Failed to select date '{target_date_str}': {e}")
            raise
        finally:
            # 5. Always switch back to the main document
            self.switch_to_default_content()


    def get_selected_date_simple_from_input(self) -> str:
        """
        Retrieves the value attribute of the date picker input field.
        Returns:
            str: The selected date as a string (e.g., '08/08/2025').
        """
        self.switch_to_frame(DemoDatePickerPageLocators.simple_date_picker_demo_iframe)
        try:
            date_value = self.get_element_attribute(
                DemoDatePickerPageLocators.date_field_locator,
                "value"
            )
            self.logger.info(f"Retrieved date value from input: '{date_value}'")
            return date_value
        finally:
            self.switch_to_default_content()





    def select_dropdown_datepicker_date(self, target_date_str: str):
        """
        Selects a date from the jQuery UI date picker.
        Args:
            target_date_str: The date to select in "YYYY-MM-DD" format.
        """
        self.switch_to_frame(DemoDatePickerPageLocators.dropdown_datepicker_demo_iframe)
        try:
            self.logger.info(f"Attempting to select date: {target_date_str}")

            # 1. Parse the target date string
            target_date = datetime.datetime.strptime(target_date_str, "%m/%d/%Y")


            # 2. Click the input field to open the date picker
            self.element_click(DemoDatePickerPageLocators.date_field_locator)

            # 3. Select the month from the dropdown
            #month_element = self.get_element(DemoDatePickerPageLocators.datepicker_month_dropdown)
            self.select_from_dropdown_by_visible_text(DemoDatePickerPageLocators.datepicker_month_dropdown, target_date.strftime("%b"))

            # 4. Select the year from the dropdown
            #year_element = self.get_element(DemoDatePickerPageLocators.datepicker_year_dropdown)
            self.select_from_dropdown_by_value(DemoDatePickerPageLocators.datepicker_year_dropdown, str(target_date.year))

            # 5. Select the day
            day_locator = self.get_dynamic_locator(
                DemoDatePickerPageLocators.datepicker_day_by_number,
                str(target_date.day)
            )
            self.element_click(day_locator)
            self.logger.info(f"Successfully selected date '{target_date_str}'.")

        except (NoSuchElementException, TimeoutException) as e:
            self.logger.error(f"Failed to select date '{target_date_str}': {e}")
            raise
        finally:
            self.switch_to_default_content()



    def get_dropdown_datepicker_selected_date_from_input(self) -> str:
        """
        Retrieves the value attribute of the date picker input field.
        Returns:
            str: The selected date as a string (e.g., '08/08/2025').
        """
        self.switch_to_frame(DemoDatePickerPageLocators.dropdown_datepicker_demo_iframe)
        try:
            date_value = self.get_element_attribute(
                DemoDatePickerPageLocators.date_field_locator,
                "value"
            )
            self.logger.info(f"Retrieved date value from input: '{date_value}'")
            return date_value
        finally:
            self.switch_to_default_content()


    def click_icon_calendar(self):


        self.switch_to_frame(DemoDatePickerPageLocators.icon_trigger_demo_iframe)
        try:
            self.element_click(DemoDatePickerPageLocators.icon_calendar_locator)

        finally:
            self.switch_to_default_content() # Always switch back



    def select_icon_triggered_simple_date(self, target_date_str: str):
        """
        Selects a date from the jQuery UI date picker.
        Args:
            target_date_str: The date to select in "YYYY-MM-DD" format.
        """
        self.switch_to_frame(DemoDatePickerPageLocators.icon_trigger_demo_iframe)
        try:
            self.logger.info(f"Attempting to select date: {target_date_str}")

            # 1. Parse the target date string
            target_date = datetime.datetime.strptime(target_date_str, "%m/%d/%Y")

            # 2. Click the input field to open the date picker
            self.element_click(DemoDatePickerPageLocators.date_field_locator)

            # 3. Navigate to the correct month and year
            while True:
                current_month = self.retrieve_element_text(DemoDatePickerPageLocators.datepicker_month)
                current_year = self.retrieve_element_text(DemoDatePickerPageLocators.datepicker_year)

                # Check if we are in the correct month and year
                if current_month == target_date.strftime("%B") and current_year == str(target_date.year):
                    self.logger.info(f"Now in the correct month/year: {current_month} {current_year}")
                    break

                # If not, navigate forward or backward
                current_date = datetime.datetime.strptime(f"{current_year}-{current_month}", "%Y-%B")
                if target_date > current_date:
                    self.logger.info(f"Moving to next month...")
                    self.element_click(DemoDatePickerPageLocators.datepicker_next_button)
                else:
                    self.logger.info(f"Moving to previous month...")
                    self.element_click(DemoDatePickerPageLocators.datepicker_prev_button)
                time.sleep(1)
            # 4. Select the day
            # Use a dynamic locator to find the day link by its text (the day number)
            day_locator = self.get_dynamic_locator(
                DemoDatePickerPageLocators.datepicker_day_by_number,
                str(target_date.day)
            )
            self.element_click(day_locator)
            self.logger.info(f"Successfully selected day: {target_date.day}")

        except (NoSuchElementException, TimeoutException) as e:
            self.logger.error(f"Failed to select date '{target_date_str}': {e}")
            raise
        finally:
            # 5. Always switch back to the main document
            self.switch_to_default_content()

    def get_icon_triggered_date_simple_from_input(self) -> str:
        """
        Retrieves the value attribute of the date picker input field.
        Returns:
            str: The selected date as a string (e.g., '08/08/2025').
        """
        self.switch_to_frame(DemoDatePickerPageLocators.icon_trigger_demo_iframe)
        try:
            date_value = self.get_element_attribute(
                DemoDatePickerPageLocators.date_field_locator,
                "value"
            )
            self.logger.info(f"Retrieved date value from input: '{date_value}'")
            return date_value
        finally:
            self.switch_to_default_content()
