from pages.BasePage import BasePage
from pages.Header_Components import HeaderComponent
from locators.demosite_dialogbox_page_locators import DemoDialogBoxPageLocators
import time
import pytest

class DemoDialogBoxPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.demoDialogBoxPageLocators = DemoDialogBoxPageLocators()

    def _click_tab(self, tab_locator: list):
        """
        Internal method to click on a tab.
        """
        self.logger.info(f"Clicking the tab with locator: {tab_locator}")
        self.element_click(tab_locator)
        time.sleep(2)

    def _get_tab_class(self, tab_locator: list) -> str:
        """
        Internal method to retrieve the 'class' attribute of a tab.
        """
        self.logger.info(f"Retrieving class attribute for tab with locator: {tab_locator}")
        return self.get_element_attribute(tab_locator, "class")

    def verify_tab_becomes_active_by_name(self, tab_name: str):
        """
        Verifies that a given tab becomes active when clicked, based on its name.
        This method maps the string name to the correct locator internally.

        The method now handles cases where the target tab is already active initially.
        """
        tab_locators = {
            "message_box_tab": DemoDialogBoxPageLocators.messagebox_tab,
            "confirmation_tab": DemoDialogBoxPageLocators.confirmationbox_tab,
            "form_tab": DemoDialogBoxPageLocators.form_tab
        }

        if tab_name not in tab_locators:
            pytest.fail(f"FAIL: Invalid tab name provided: '{tab_name}'")

        tab_locator = tab_locators[tab_name]
        self.logger.info(f"Starting verification for '{tab_name}' tab activation.")

        # Check if the target tab is already active. If so, click a different tab
        # to ensure the test starts from a known inactive state.
        if self._get_tab_class(tab_locator) == "resp-tab-item resp-tab-active":
            self.logger.info(f"The '{tab_name}' tab is already active. Clicking a different tab to reset state.")

            # Find and click a different tab (e.g., the first one in the list)
            other_tab_locator = None
            for name, locator in tab_locators.items():
                if name != tab_name:
                    other_tab_locator = locator
                    break

            if other_tab_locator:
                self._click_tab(other_tab_locator)
            else:
                pytest.fail("Could not find an alternative tab to click to reset state.")

        # 1. Get the initial class and assert it is not the active class
        initial_class = self._get_tab_class(tab_locator)
        assert initial_class == "resp-tab-item", \
            f"FAIL: Tab should not be active initially. Got: {initial_class}"

        # 2. Click the tab using the generic click method
        self._click_tab(tab_locator)

        # 3. Get the new class and assert it has become active
        new_class = self._get_tab_class(tab_locator)
        expected_class = "resp-tab-item resp-tab-active"
        assert new_class == expected_class, \
            f"FAIL: Tab did not become active. Expected: '{expected_class}', Got: '{new_class}'"

        self.logger.info(f"SUCCESS: Tab '{tab_name}' correctly became active after click.")

    # These older methods can remain for backwards compatibility if needed
    def click_message_box_tab(self):
        self._click_tab(DemoDialogBoxPageLocators.messagebox_tab)

    def click_confirmation_tab(self):
        self._click_tab(DemoDialogBoxPageLocators.confirmationbox_tab)

    def click_form_tab(self):
        self._click_tab(DemoDialogBoxPageLocators.form_tab)

    def get_message_box_tab_class(self):
        return self._get_tab_class(DemoDialogBoxPageLocators.messagebox_tab)

    def get_confirmation_tab_class(self):
        return self._get_tab_class(DemoDialogBoxPageLocators.confirmationbox_tab)

    def get_form_tab_class(self):
        return self._get_tab_class(DemoDialogBoxPageLocators.form_tab)
