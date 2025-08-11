from pages.BasePage import BasePage
from pages.Header_Components import HeaderComponent
from locators.demosite_tabs_page_locators import DemoTabsPageLocators
import time

class DemoTabsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.demoTabsPageLocators = DemoTabsPageLocators()

    def expandSectionThree(self):
        self.switch_to_frame(self.demoTabsPageLocators.demo_iframe)
        self.element_click(self.demoTabsPageLocators.section_three_locator)
        is_expanded = self.wait_for_attribute_value_to_be(
            locators=self.demoTabsPageLocators.section_three_locator,
            attribute="aria-expanded",
            expected_value="true"
        )
        self.switch_to_default_content()
        return is_expanded

