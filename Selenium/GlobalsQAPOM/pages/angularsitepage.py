from pages.BasePage import BasePage
from pages.Header_Components import HeaderComponent
from locators.angularjs_page_locators import AngularJSLocators
import time

class AngularJSPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.AngularJSLocators = AngularJSLocators()

    def gotoMultiForm(self):
        from pages.angularjs_multiformPage import AngularJSMultiFormPage
        self.element_click(AngularJSLocators.multiform_locator)
        return AngularJSMultiFormPage(self.driver)
