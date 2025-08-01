from pages.BasePage import BasePage
from pages.Header_Components import HeaderComponent
from locators.demosite_page_locators import DemoSitePageLocators
import time

class DemoPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.demoSitePageLocators = DemoSitePageLocators()

    def gotoTabs(self):
        from pages.demosite_TabsPage import DemoTabsPage
        self.element_click(self.demoSitePageLocators.tabs_locator)
        return DemoTabsPage(self.driver)


    def gotoSlider(self):
        from pages.demosite_SliderPage import DemoSliderPage
        self.element_click(self.demoSitePageLocators.slider_locator)
        return DemoSliderPage(self.driver)

    def gotoToolTip(self):
        from pages.demosite_ToolTipPage import DemoToolTipPage
        self.element_click(self.demoSitePageLocators.tooltip_locator)
        return DemoToolTipPage(self.driver)

    def gotoAlertBox(self):
        from pages.demosite_AlertBoxPage import DemoAlertBoxPage
        self.element_click(self.demoSitePageLocators.tooltip_locator)
        return DemoAlertBoxPage(self.driver)

    def gotoDialogBox(self):
        from pages.demosite_DialogBoxPage import DemoDialogBoxPage
        self.element_click(self.demoSitePageLocators.dialogbox_locator)
        return DemoDialogBoxPage(self.driver)
