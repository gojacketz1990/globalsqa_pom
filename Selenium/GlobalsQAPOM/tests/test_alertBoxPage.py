import pytest
import time
from pages.globalsqa_mainpage import GlobalsqaMainPage

@pytest.mark.usefixtures("setup_globalsqa")
class TestAlertBox:
    def test_visible_tooltips_display_correct_text(self):
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()
        demoAlertBoxPage = demoPage.gotoAlertBox()

        #This doesn't seem to be working on globalsa right now
        
