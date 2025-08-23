from pages.BasePage import BasePage
from pages.Header_Components import HeaderComponent
from locators.demosite_spinner_page_locator import DemoSpinnerPageLocators
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
import time
import pytest
import re

class DemoSpinnerPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.demoSpinnerPageLocators = DemoSpinnerPageLocators()
        self.logger = self.getLogger()

    def _click_tab(self, tab_locator: list):
        """
        Internal method to click on a tab.
        """

        self.logger.info(f"Clicking the tab with locator: {tab_locator}")
        self.element_click(tab_locator)
        time.sleep(2)

    def click_currency_tab(self):
        self._click_tab(DemoSpinnerPageLocators.click_currency_tab_locator)

    def click_simple_spinner_tab(self):
        self._click_tab(DemoSpinnerPageLocators.click_simple_spinner_tab_locator)
    #
    # def set_currency(self,currency):
    #     self.select_from_dropdown_by_value(DemoSpinnerPageLocators.currency_dropdown_locator, currency)

    def select_currency_from_dropdown_by_value(self, currency: str):
        """
        Selects a country from the dropdown by its 'value' attribute.

        Args:
            country_value (str): The 'value' attribute of the country option
                                 (e.g., 'AFG' for Afghanistan, 'ALB' for Albania).
        """
        self.switch_to_frame(DemoSpinnerPageLocators.demo_iframe)
        try:
            self.element_click(DemoSpinnerPageLocators.currency_dropdown_locator)
            self.select_from_dropdown_by_value(
                DemoSpinnerPageLocators.currency_dropdown_locator,
                currency
            )
            self.logger.info(f"Selected country with value '{currency}' from the dropdown.")
        finally:
            self.switch_to_default_content() # Always switch back


    def get_current_spinner_value(self) -> int:
        """
        Retrieves the current value of the spinner by getting its 'aria-valuenow' attribute.

        Returns:
            int: The current value of the spinner.
        """
        self.logger.info("Getting current spinner value.")
        self.switch_to_frame(DemoSpinnerPageLocators.demo_iframe)
        try:
            value_str = self.get_element_attribute(DemoSpinnerPageLocators.amount_spinner_locator, "aria-valuenow")
            self.logger.info(f"Retrieved spinner value: {value_str}")
            return int(value_str) # Convert to integer
        except Exception as e:
            self.logger.error(f"Failed to get spinner value: {e}")
            raise
        finally:
            self.switch_to_default_content() # Always switch back


    def click_spinner_button(self, direction: str):
        """
        Clicks either the 'up' or 'down' spinner button.

        Args:
            direction (str): The direction to click, either "up" or "down".
        """
        self.logger.info(f"Attempting to click spinner '{direction}' button. ⬆️⬇️")
        # Switch to the iframe if the spinner is inside one
        # Assumes self.locators.spinner_iframe_locator is defined and correct
        self.switch_to_frame(DemoSpinnerPageLocators.demo_iframe)
        try:
            if direction.lower() == "up":
                # Assumes self.locators.up_spinner_button_locator is defined
                self.element_click(DemoSpinnerPageLocators.up_amount_locator)
                self.logger.info("Clicked spinner 'up' button.")
            elif direction.lower() == "down":
                # Assumes self.locators.down_spinner_button_locator is defined
                self.element_click(DemoSpinnerPageLocators.down_amount_locator)
                self.logger.info("Clicked spinner 'down' button.")
            else:
                raise ValueError("Invalid direction. Please use 'up' or 'down'.")
        except Exception as e:
            self.logger.error(f"Failed to click spinner '{direction}' button: {e}")
            raise
        finally:
            # Always switch back to the default content
            self.switch_to_default_content()




    def get_current_simple_spinner_value(self) -> int:
        """
        Retrieves the current value of the spinner by getting its 'aria-valuenow' attribute.

        Returns:
            int: The current value of the spinner.
        """
        self.logger.info("Getting current spinner value.")
        self.switch_to_frame(DemoSpinnerPageLocators.simple_spinner_iframe_locator)
        try:
            value_str = self.get_element_attribute(DemoSpinnerPageLocators.amount_spinner_locator, "aria-valuenow")
            self.logger.info(f"Retrieved spinner value: {value_str}")
            return int(value_str) # Convert to integer
        except Exception as e:
            self.logger.error(f"Failed to get spinner value: {e}")
            raise
        finally:
            self.switch_to_default_content() # Always switch back

    def click_simple_spinner_button(self, direction: str):
        """
        Clicks either the 'up' or 'down' spinner button.

        Args:
            direction (str): The direction to click, either "up" or "down".
        """
        self.logger.info(f"Attempting to click spinner '{direction}' button. ⬆️⬇️")
        # Switch to the iframe if the spinner is inside one
        # Assumes self.locators.spinner_iframe_locator is defined and correct
        self.switch_to_frame(DemoSpinnerPageLocators.simple_spinner_iframe_locator)
        try:
            if direction.lower() == "up":
                # Assumes self.locators.up_spinner_button_locator is defined
                self.element_click(DemoSpinnerPageLocators.up_amount_locator)
                self.logger.info("Clicked spinner 'up' button.")
            elif direction.lower() == "down":
                # Assumes self.locators.down_spinner_button_locator is defined
                self.element_click(DemoSpinnerPageLocators.down_amount_locator)
                self.logger.info("Clicked spinner 'down' button.")
            else:
                raise ValueError("Invalid direction. Please use 'up' or 'down'.")
        except Exception as e:
            self.logger.error(f"Failed to click spinner '{direction}' button: {e}")
            raise
        finally:
            # Always switch back to the default content
            self.switch_to_default_content()

    def toggle_disable_engage(self):
        """
        Clicks the button that toggles the spinner's enabled/disabled state.
        """
        self.logger.info("Clicking the spinner toggle disable button.")
        # Switch to the iframe as the toggle button is located within it
        self.switch_to_frame(DemoSpinnerPageLocators.simple_spinner_iframe_locator)
        try:
            self.element_click(DemoSpinnerPageLocators.toggle_button_locator)
            self.logger.info("Clicked the spinner toggle disable button.")
        except Exception as e:
            self.logger.error(f"Failed to click spinner toggle disable button: {e}")
            raise
        finally:
            # Always switch back to the default content
            self.switch_to_default_content()



    def toggle_widget(self):
        self.element_click(DemoSpinnerPageLocators.toggle_widget_button_locator)

    def click_get_value_button(self):
        self.element_click(DemoSpinnerPageLocators.get_value_button_locator)


    def click_set_value_to_five_button(self):
        self.element_click(DemoSpinnerPageLocators.set_value_to_5_button_locator)

    def is_spinner_input_disabled(self) -> bool:
        """
        Checks if the spinner's input field is disabled.
        It checks for the 'disabled' attribute.
        """
        self.logger.info("Checking if spinner input is disabled.")
        self.switch_to_frame(DemoSpinnerPageLocators.simple_spinner_iframe_locator)
        try:
            # Check for the 'disabled' attribute directly on the input
            input_element = self.get_element(DemoSpinnerPageLocators.amount_spinner_locator)
            is_disabled = input_element.get_attribute("disabled") is not None
            self.logger.info(f"Spinner input disabled state: {is_disabled}")
            return is_disabled
        except Exception as e:
            self.logger.error(f"Failed to check spinner input disabled state: {e}")
            raise
        finally:
            self.switch_to_default_content()

    def are_spinner_buttons_disabled(self) -> bool:
        """
        Checks if both the 'up' and 'down' spinner buttons have the 'ui-state-disabled' class.
        """
        self.logger.info("Checking if spinner buttons are disabled.")
        self.switch_to_frame(DemoSpinnerPageLocators.simple_spinner_iframe_locator)
        try:
            up_button = self.get_element(DemoSpinnerPageLocators.up_amount_locator)
            down_button = self.get_element(DemoSpinnerPageLocators.down_amount_locator)

            up_disabled = "ui-state-disabled" in up_button.get_attribute("class")
            down_disabled = "ui-state-disabled" in down_button.get_attribute("class")

            self.logger.info(f"Up button disabled: {up_disabled}, Down button disabled: {down_disabled}")
            return up_disabled and down_disabled
        except Exception as e:
            self.logger.error(f"Failed to check spinner button disabled state: {e}")
            raise
        finally:
            self.switch_to_default_content()
