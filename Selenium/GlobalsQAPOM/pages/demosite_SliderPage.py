from pages.BasePage import BasePage
from pages.Header_Components import HeaderComponent
from locators.demosite_slider_page_locators import DemoSliderPageLocators
import time

class DemoSliderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.demoSliderPageLocators = DemoSliderPageLocators()

    def move_slider_by_color(self, color, offset):
            self.switch_to_frame(self.demoSliderPageLocators.demo_iframe)
            """
            Move slider of the given color by offset (pixels or value).
            """
            if color.lower() == "red":
                locator = self.demoSliderPageLocators.red_slider_locator
            elif color.lower() == "green":
                locator = self.demoSliderPageLocators.green_slider_locator
            elif color.lower() == "blue":
                locator = self.demoSliderPageLocators.blue_slider_locator
            else:
                raise ValueError(f"Unknown slider color: {color}")

            slider_handle = self.get_element_clickable(locator)
            self.drag_element_by_offset(slider_handle, offset, 0)
            self.switch_to_default_content()


