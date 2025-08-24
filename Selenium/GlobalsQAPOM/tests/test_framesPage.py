import pytest
from pages.globalsqa_mainpage import GlobalsqaMainPage
import time
from utilities.LoggerBase import LoggerBase
@pytest.mark.usefixtures("setup_globalsqa")
class TestFrames:

    def test_verify_link_in_iframe(self, logger):
        """
        Verifies that clicking the 'Start Download' button makes the
        file download dialog box appear.
        """
        logger.info("Starting test_verify_link_in_iframe test")
        # Instantiate page objects
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoFramesPage = demoPage.gotoFrames()

        demoFramesPage.click_iframe_tab()


        is_text_in_iframe_present = demoFramesPage.test_click_link_in_iframe()

        assert is_text_in_iframe_present, "Failed to verify that the text appears."



    def test_verify_new_tab(self, logger):
        """
        Verifies that clicking the 'Start Download' button makes the
        file download dialog box appear.
        """
        logger.info("Starting test_verify_new_tab test")
        # Instantiate page objects
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoFramesPage = demoPage.gotoFrames()

        demoFramesPage.click_open_new_browserwindow_tab()
        time.sleep(2)
        demoFramesPage.click_iframe_tab()
        time.sleep(2)
        demoFramesPage.click_open_new_browsertab_tab()
        time.sleep(2)


        demoFramesPage.click_open_new_bowser_tab_button()

        is_new_tab_opened = demoFramesPage.verify_new_browser_tab_opens()

        assert is_new_tab_opened, "Failed to verify that a new tab opened."


