from pages.BasePage import BasePage
from pages.Header_Components import HeaderComponent
from locators.angularjs_simplecalculator_locators import AngularJSSearchFilterPageLocators
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
import time
import datetime
import pytest
import re
import json

class AngularJSSimpleCaculatorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.angularJSSearchFilterPageLocators = AngularJSSearchFilterPageLocators()


    def get_calculation_details(self) -> list:
        """Retrieves the numbers and result from the calculation text."""
        # Get the full text, e.g., "14 - 25 = -11"
        result_text = self.retrieve_element_text(AngularJSSearchFilterPageLocators.calculation_result)
        self.logger.info(f"Retrieved calculation text: '{result_text}'")

        # Split the text by spaces
        # This will result in a list like ['14', '-', '25', '=', '-11']
        details = result_text.split()

        return details

    def enter_a_value(self,a):
        self.type_into_element(a,AngularJSSearchFilterPageLocators.a_input_locator)

    def enter_b_value(self,b):
        self.type_into_element(b,AngularJSSearchFilterPageLocators.b_input_locator)

    def select_operation(self, operation):
        self.select_from_dropdown_by_visible_text(AngularJSSearchFilterPageLocators.operation_dropdown, operation)

    def perform_calculation(self,a,b,operation):
        self.enter_a_value(a)
        self.enter_b_value(b)
        self.select_operation(operation)
