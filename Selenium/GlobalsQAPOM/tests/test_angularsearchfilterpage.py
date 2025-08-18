import pytest
from pages.globalsqa_mainpage import GlobalsqaMainPage
import time

@pytest.mark.usefixtures("setup_globalsqa")
class TestSearchFilter:

    def test_searchfilter(self):

        from utilities.FakerHelper import FakerHelper
        data_generator = FakerHelper(locale='en_US')

        globalsqaPage = GlobalsqaMainPage(self.driver)
        angularjsPage = globalsqaPage.header.gotoAngularSitePage()

        searchfilterPage = angularjsPage.gotoSearchFilter()
