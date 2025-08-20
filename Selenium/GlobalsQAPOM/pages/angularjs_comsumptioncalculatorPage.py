from pages.BasePage import BasePage
from pages.Header_Components import HeaderComponent
from locators.angularjs_comsumption_calculator_locators import AngularJSConsumptionCalculatorPageLocators
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
import time
import datetime
import pytest
import re
import json

class AngularJSConsumptionCalculatorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.angularJSConsumptionCalculatorPageLocators = AngularJSConsumptionCalculatorPageLocators()

    def enter_cups_of_coffee(self, quantity: int):
        """Enters the specified quantity of cups of coffee."""
        self.logger.info(f"Entering {quantity} cups of coffee.")
        self.type_into_element(str(quantity), AngularJSConsumptionCalculatorPageLocators.coffee_input)

    def enter_cigarettes(self, quantity: int):
        """Enters the specified quantity of cigarettes."""
        self.logger.info(f"Entering {quantity} cigarettes.")
        self.type_into_element(str(quantity), AngularJSConsumptionCalculatorPageLocators.cigarettes_input)

    def get_total_caffeine(self) -> float:
        """Retrieves the total milligrams of caffeine."""
        total_mg = self.get_element_attribute(AngularJSConsumptionCalculatorPageLocators.caffeine_total, "value")
        self.logger.info(f"Retrieved total caffeine: {total_mg}mg")
        return float(total_mg)

    def get_total_tar(self) -> float:
        """Retrieves the total milligrams of tar."""
        total_mg = self.get_element_attribute(AngularJSConsumptionCalculatorPageLocators.tar_total, "value")
        self.logger.info(f"Retrieved total tar: {total_mg}mg")
        return float(total_mg)

    def is_caffeine_limit_exceeded(self) -> bool:
        """Checks if the daily caffeine limit warning is visible."""
        try:
            # Find the element first
            warning_element = self.get_element(AngularJSConsumptionCalculatorPageLocators.caffeine_limit_warning)

            # CORRECTED: Use .is_displayed() to check for visibility
            is_exceeded = warning_element.is_displayed()

            self.logger.info(f"Caffeine limit exceeded: {is_exceeded}")
            return is_exceeded
        except NoSuchElementException:
            # If the element isn't even in the DOM, it's not displayed
            return False

    def is_tar_limit_exceeded(self) -> bool:
        """Checks if the daily tar limit warning is visible."""
        try:
            warning_element = self.get_element(AngularJSConsumptionCalculatorPageLocators.tar_limit_warning)
            is_exceeded = warning_element.is_displayed()
            self.logger.info(f"Tar limit exceeded: {is_exceeded}")
            return is_exceeded
        except NoSuchElementException:
            return False
