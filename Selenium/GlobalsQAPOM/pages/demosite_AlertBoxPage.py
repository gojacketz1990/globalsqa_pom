from pages.BasePage import BasePage
from pages.Header_Components import HeaderComponent
from locators.demosite_alertBox_page_locators import DemoAlertBoxPageLocators
import time

class DemoAlertBoxPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.demoAlertBoxPageLocators = DemoAlertBoxPageLocators()
