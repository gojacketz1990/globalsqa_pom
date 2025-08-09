from pages.BasePage import BasePage
from pages.Header_Components import HeaderComponent
from locators.demosite_tool_tips_page_locators import DemoToolTipPageLocators
import time

class DemoToolTipPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.demoToolTipPageLocators = DemoToolTipPageLocators()


    def hover_and_get_title_tooltip(self, locators):
        """Hover over element and get its title attribute (classic tooltip)."""
        self.switch_to_frame(self.demoToolTipPageLocators.demo_iframe)
        element = self.get_element(locators)
        self.hover_over_element(locators)
        tooltip_text = element.get_attribute("title")
        self.switch_to_default_content()
        return tooltip_text

    def hover_and_get_visible_tooltip_text(self, target_locator):
        self.switch_to_frame(self.demoToolTipPageLocators.demo_iframe)

        # Hover over the target element
        target_element = self.get_element(target_locator)
        self.hover_over_element(target_locator)
        time.sleep(3)

        # Wait for tooltip to become visible and get its text
        tooltip = self.wait_for_element_to_be_visible(
            self.demoToolTipPageLocators.tooltip_element_locator
        )
        text = tooltip.text

        self.switch_to_default_content()
        return text
