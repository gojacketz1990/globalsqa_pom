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

    def gotoWebTable(self):
        from pages.angularjs_webtablePage import AngularJSWebTablePage
        self.element_click(AngularJSLocators.webtable_locator)
        return AngularJSWebTablePage(self.driver)

    def gotoSearchFilter(self):
        from pages.angularjs_searchfilterPage import AngularJSSearchFilterPage
        self.element_click(AngularJSLocators.searchfilter_locator)
        return AngularJSSearchFilterPage(self.driver)

    def gotoScrollable(self):
        from pages.angularjs_scrollablePage import AngularJSScrollablePage
        self.element_click(AngularJSLocators.scrollable_locator)
        return AngularJSScrollablePage(self.driver)

    def gotoRegistrationLogin(self):
        from pages.angularjs_registrationLoginPage import AngularJSRegistrationLoginPage
        self.element_click(AngularJSLocators.registration_login_locator)
        return AngularJSRegistrationLoginPage(self.driver)

    def gotoUploadImage(self):
        from pages.angularjs_uploadimagePage import AngularJSUploadImagePage
        self.element_click(AngularJSLocators.upload_image_locator)
        return AngularJSUploadImagePage(self.driver)

    def gotoBankingProject(self):
        from pages.angularjs_bankingprojectPage import AngularJSBankingProjectPage
        self.element_click(AngularJSLocators.banking_project_locator)
        return AngularJSBankingProjectPage(self.driver)
