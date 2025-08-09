from pages.BasePage import BasePage
from pages.Header_Components import HeaderComponent
from locators.demosite_dropdown_page_locators import DemoDropDownPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import pytest

class DemoDropDownPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.demoDropDownPageLocators = DemoDropDownPageLocators()

    def select_country_from_dropdown(self,country):
        self.select_from_dropdown_by_visible_text(DemoDropDownPageLocators.country_dropdown_locator,country)

    def get_selected_country_text(self):
        """Returns the text of the currently selected country."""
        return self.get_dropdown_selected_option_text(self.demoDropDownPageLocators.country_dropdown_locator)

    def is_dropdown_visible(self):
        """Checks if the country dropdown is visible."""
        return self.check_display_status_of_element(self.demoDropDownPageLocators.country_dropdown_locator)


    def get_dropdown_options(self):
        """Returns a list of all country options in the dropdown."""
        return self.get_elements(self.demoDropDownPageLocators.country_options_locator)

    def is_option_present(self, option_text):
        """Checks if a specific option is present in the dropdown list."""
        all_options = self.get_dropdown_options()
        for option in all_options:
            if option.text.strip() == option_text:
                return True
        return False

    def click_dropdownown(self):
        """Returns a list of all country options in the dropdown."""
        self.element_click(self.demoDropDownPageLocators.country_options_locator)
