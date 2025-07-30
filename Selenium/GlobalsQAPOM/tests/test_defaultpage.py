import pytest
import time
from pages.globalsqa_mainpage import GlobalsqaMainPage

@pytest.mark.usefixtures("setup_globalsqa")
class TestMethods():

    def test_gotoDemoPage(self):

        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()
        demoPage.gotoTabs()

        time.sleep(3)



    # def test_gotoAngularPage(self):
    #
    #     globalsqaPage = GlobalsqaMainPage(self.driver)
    #     globalsqaPage.gotoAngularSitePage()
    #     time.sleep(3)
    #
    #
