import pytest
from pages.globalsqa_mainpage import GlobalsqaMainPage
import time
from utilities.LoggerBase import LoggerBase
@pytest.mark.usefixtures("setup_globalsqa")
class TestMultiForm(LoggerBase):

    def test_scrollable(self, logger):
        logger.info("Starting test_scrollable test")

        globalsqaPage = GlobalsqaMainPage(self.driver)
        angularjsPage = globalsqaPage.header.gotoAngularSitePage()

        scrollablePage = angularjsPage.gotoScrollable()

        time.sleep(3)

        # Call the new method to find the user
        user_found = scrollablePage.find_user_by_scrolling("JACQUES", "Delcourt")

        # Assert that the user was found
        assert user_found, "The specified user was not found after scrolling."

#Need to add tests for sorting
