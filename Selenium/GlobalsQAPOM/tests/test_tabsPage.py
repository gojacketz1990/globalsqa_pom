import pytest
import time
from pages.globalsqa_mainpage import GlobalsqaMainPage

@pytest.mark.usefixtures("setup_globalsqa")
class TestTabs():

     def test_expandtabs(self):
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()
        demoTabsPage = demoPage.gotoTabs()
        success = demoTabsPage.expandSectionThree()
        assert success, "Accordion section three should expand"
        time.sleep(3)  # optional, better to wait dynamically
