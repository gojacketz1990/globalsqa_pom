from pages.BasePage import BasePage
from pages.Header_Components import HeaderComponent
from locators.demosite_tabs_page_locators import DemoTabsPageLocators
import time

class DemoTabsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.demoTabsPageLocators = DemoTabsPageLocators()

    def expandSectionThree(self):
        #The Accordians and Tabs section is in an iFrame:
        self.switch_to_frame(self.demoTabsPageLocators.demo_iframe)
        self.element_click(self.demoTabsPageLocators.section_three_locator)
                # Now, call your new method to verify the state change
        is_expanded = self.wait_for_attribute_value_to_be(
            locators=self.demoTabsPageLocators.section_three_locator,
            attribute="aria-expanded",
            expected_value="true"
        )

        if not is_expanded:
            raise AssertionError("Accordion section did not expand as expected.")

        self.switch_to_default_content()
