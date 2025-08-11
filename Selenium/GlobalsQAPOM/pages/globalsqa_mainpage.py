from pages.BasePage import BasePage
from locators.globalsqa_main_page_locators import globalsqamain_locators
from pages.Header_Components import HeaderComponent



class GlobalsqaMainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.globalsqamain_locators = globalsqamain_locators()
        self.header = HeaderComponent(driver)

