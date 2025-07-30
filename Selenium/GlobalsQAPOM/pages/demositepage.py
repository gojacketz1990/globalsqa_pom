from pages.BasePage import BasePage
from pages.Header_Components import HeaderComponent
from locators.demosite_page_locators import DemoSitePageLocators
import time

class DemoPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.demoSitePageLocators = DemoSitePageLocators()

    def gotoTabs(self):
        self.element_click(self.demoSitePageLocators.tabs_locator)
