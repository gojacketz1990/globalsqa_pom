import pytest
from pages.globalsqa_mainpage import GlobalsqaMainPage
import time

@pytest.mark.usefixtures("setup_globalsqa")
class TestWebTable:

    def test_webtable(self):

        from utilities.FakerHelper import FakerHelper
        data_generator = FakerHelper(locale='en_US')

        globalsqaPage = GlobalsqaMainPage(self.driver)
        angularjsPage = globalsqaPage.header.gotoAngularSitePage()

        webtablePage = angularjsPage.gotoWebTable()

        webtablePage.first_name_search("Jac")

        time.sleep(3)

        webtablePage.global_search("Jac")

        time.sleep(3)
