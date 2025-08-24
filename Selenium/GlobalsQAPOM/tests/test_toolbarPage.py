import pytest
from pages.globalsqa_mainpage import GlobalsqaMainPage
import time
from utilities.LoggerBase import LoggerBase

@pytest.mark.usefixtures("setup_globalsqa")
class TestToolbar(LoggerBase):

    def test_change_and_verify_font_size(self, logger):
        logger.info("Starting test_change_and_verify_font_size test")
        """
        Verifies that clicking the 'Start Download' button makes the
        file download dialog box appear.
        """

        # Instantiate page objects
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoToolbarPage = demoPage.gotoToolBar()

        #demoSpinnerPage.click_simple_spinner_tab()
        #time.sleep(2)
        demoToolbarPage.click_toolbar_tab()

        demoToolbarPage.select_text_and_font_size("18px")

        time.sleep(5)

        # Assertion: Verify that the font size is 18px
        checkfontsize = demoToolbarPage.verify_font_tag_size_attribute("7")

        assert checkfontsize is True, f"The font size should be 7 but it is not."

        # Example usage in a test file or another page object
        # Assuming 'driver' is your WebDriver instance

    def test_run_last_action_button(self):

        # Instantiate page objects
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoToolbarPage = demoPage.gotoToolBar()

        #demoSpinnerPage.click_simple_spinner_tab()
        #time.sleep(2)
        demoToolbarPage.click_splitbutton_tab()

        demoToolbarPage.click_run_last_option_button()

        # To select "Save":
        #demoToolbarPage.select_action_from_dropdown("Save")

        # To select "Open...":
        # demo_toolbar_page.select_action_from_dropdown("Open...")

        # To select "Delete":
        # demo_toolbar_page.select_action_from_dropdown("Delete")

        time.sleep(3)


    def test_select_action(self):

        # Instantiate page objects
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoToolbarPage = demoPage.gotoToolBar()

        #demoSpinnerPage.click_simple_spinner_tab()
        #time.sleep(2)
        demoToolbarPage.click_splitbutton_tab()


        # To select "Save":
        demoToolbarPage.select_action_from_dropdown("Save")
        time.sleep(3)

        # To select "Open...":
        # demo_toolbar_page.select_action_from_dropdown("Open...")

        # To select "Delete":
        # demo_toolbar_page.select_action_from_dropdown("Delete")
        captured_list = demoToolbarPage.get_all_output_texts()
        expected_list = ["Save"]
        assert captured_list == expected_list, f"Expected list {expected_list} but got {captured_list}"

        demoToolbarPage.click_run_last_option_button()

        time.sleep(3)

        captured_list = demoToolbarPage.get_all_output_texts()

        #expected_list = ["Save", "Delete", "Running Last Action..."]
        expected_list = ["Save", "Running Last Action..."]
        assert captured_list == expected_list, f"Expected list {expected_list} but got {captured_list}"
