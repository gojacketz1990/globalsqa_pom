from pages.BasePage import BasePage
from pages.Header_Components import HeaderComponent
from locators.demosite_sample_page_locators import DemoSamplePageLocators
from selenium.common.exceptions import TimeoutException
import time
import pytest
import re

class DemoSamplePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.demoSamplePageLocators = DemoSamplePageLocators()

    def _get_expertise_checkbox_parent(self):
        """Private helper to get the parent container for the expertise checkboxes."""
        return self.get_element(DemoSamplePageLocators.expertise_checkbox_parent_locator)

    def select_expertise_by_label(self, label_text: str):
        """
        Selects an expertise checkbox if it is not already selected.

        Args:
            label_text (str): The text of the label (e.g., "Automation Testing").
        """
        parent = self._get_expertise_checkbox_parent()

        # Use the dynamic locator to find the specific checkbox
        dynamic_locator = self.get_dynamic_locator(
            DemoSamplePageLocators.expertise_checkbox_label_text_locator,
            label_text
        )

        checkbox = self.get_child_element(parent, dynamic_locator)

        if not checkbox.is_selected():
            checkbox.click()
            self.logger.info(f"Selected checkbox for: {label_text}")
        else:
            self.logger.info(f"Checkbox for '{label_text}' was already selected.")

    def deselect_expertise_by_label(self, label_text: str):
        """
        Deselects an expertise checkbox if it is already selected.

        Args:
            label_text (str): The text of the label (e.g., "Automation Testing").
        """
        parent = self._get_expertise_checkbox_parent()
        dynamic_locator = self.get_dynamic_locator(
            DemoSamplePageLocators.expertise_checkbox_label_text_locator,
            label_text
        )

        checkbox = self.get_child_element(parent, dynamic_locator)

        if checkbox.is_selected():
            checkbox.click()
            self.logger.info(f"Deselected checkbox for: {label_text}")
        else:
            self.logger.info(f"Checkbox for '{label_text}' was already deselected.")

    def get_selected_expertise_values(self) -> list[str]:
        """
        Returns a list of the 'value' attributes for all selected expertise checkboxes.
        """
        parent = self._get_expertise_checkbox_parent()
        all_checkboxes = self.get_child_elements(parent, DemoSamplePageLocators.expertise_checkbox_locator)

        selected_values = []
        for checkbox in all_checkboxes:
            if checkbox.is_selected():
                selected_values.append(checkbox.get_attribute("value"))

        return selected_values

    def select_education_option(self, label_text: str):
        parent = self.get_element(DemoSamplePageLocators.education_radio_parent_locator)

        # Call BasePage's get_dynamic_locator method
        dynamic_locator = self.get_dynamic_locator(
            DemoSamplePageLocators.education_radio_label_text_locator,
            label_text
        )

        radio_button = self.get_child_element(parent, dynamic_locator)
        radio_button.click()

    def get_selected_education_option(self) -> str:
        """
        Returns the value of the currently selected radio button.
        """
        parent = self.get_element(DemoSamplePageLocators.education_radio_parent_locator)
        # Find all radio buttons within the parent
        radio_buttons = self.get_child_elements(parent, [("css", "input[type='radio']")])

        for radio in radio_buttons:
            if radio.is_selected():
                return radio.get_attribute("value")

        self.logger.warning("No radio button is currently selected in the education group.")
        return ""

    def upload_file_path(self, filePath):

       self.upload_file(DemoSamplePageLocators.choose_file_button_locator,filePath)


    def enter_name(self, name):
        self.type_into_element(name, DemoSamplePageLocators.name_text_locator)

    def enter_email(self, email):
        self.type_into_element(email, DemoSamplePageLocators.email_locator)

    def enter_website(self, website):
        self.type_into_element(website, DemoSamplePageLocators.website_locator)

    def click_alert_box(self):
        self.element_click(DemoSamplePageLocators.alert_box_button_locator)

    def dismiss_alerts(self):
        #Dismiss two popus
        self.switch_to_alert_and_accept_popup()
        self.switch_to_alert_and_accept_popup()

    def dismiss_chain_alerts(self):
        self.dismiss_all_alerts()

    def enter_comments(self, comment):
        self.type_into_element(comment, DemoSamplePageLocators.comment_text_box_locator)

    def click_submit(self):
        self.element_click(DemoSamplePageLocators.submit_button_locator)
