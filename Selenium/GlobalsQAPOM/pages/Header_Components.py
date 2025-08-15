from locators.header_locators import HeaderLocators
from pages.BasePage import BasePage

# Shared components by every page

class HeaderComponent(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.headerLocators = HeaderLocators()



    def gotoDemoSitePage(self):
        from pages.demositepage import DemoPage
        self.hover_and_click_popup(self.headerLocators.testers_hub_dropdown_locator, self.headerLocators.demo_site_link_locator)
        return DemoPage(self.driver)



    def gotoAngularSitePage(self):
        from pages.angularsitepage import AngularJSPage
        self.hover_and_click_popup(self.headerLocators.testers_hub_dropdown_locator, self.headerLocators.angular_site_link_locator)
        return AngularJSPage(self.driver)
