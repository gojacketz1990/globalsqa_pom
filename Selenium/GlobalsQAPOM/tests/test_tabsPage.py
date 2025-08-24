import pytest
import time
from pages.globalsqa_mainpage import GlobalsqaMainPage
from utilities.LoggerBase import LoggerBase

@pytest.mark.usefixtures("setup_globalsqa")
class TestTabs(LoggerBase):

     def test_expandtabs(self, logger):
        logger.info("Starting test_expandtabs test")
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()
        demoTabsPage = demoPage.gotoTabs()
        success = demoTabsPage.expandSectionThree()
        assert success, "Accordion section three should expand"
        time.sleep(3)  # optional, better to wait dynamically
