import pytest
from pages.globalsqa_mainpage import GlobalsqaMainPage
import time

@pytest.mark.usefixtures("setup_globalsqa")
class TestSimpleCalculator:

    def test_scrollable(self):

        from utilities.FakerHelper import FakerHelper
        data_generator = FakerHelper(locale='en_US')

        globalsqaPage = GlobalsqaMainPage(self.driver)
        angularjsPage = globalsqaPage.header.gotoAngularSitePage()

        simplecalculatorPage = angularjsPage.gotoSimpleCalculator()
