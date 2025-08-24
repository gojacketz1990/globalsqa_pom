import pytest
from pages.globalsqa_mainpage import GlobalsqaMainPage
import time
from utilities.LoggerBase import LoggerBase

@pytest.mark.usefixtures("setup_globalsqa")
class TestDialogBoxTabs(LoggerBase):

    def test_verify_color_change(self):
        """
        Verifies that clicking the 'Start Download' button makes the
        file download dialog box appear.
        """

        # Instantiate page objects
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoProgressBarPage = demoPage.gotoProgressBar()

        demoProgressBarPage.click_random_progress_bar_tab()

        demoProgressBarPage.test_progress_bar_color_updates()

    def test_verify_percentage_change(self):
        """
        Verifies that clicking the 'Start Download' button makes the
        file download dialog box appear.
        """

        # Instantiate page objects
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoProgressBarPage = demoPage.gotoProgressBar()

        demoProgressBarPage.click_random_progress_bar_tab()

        demoProgressBarPage.test_progress_bar_percentage_updates()

    def test_print_progress_bar_stuff(self):
        """
        Verifies that clicking the 'Start Download' button makes the
        file download dialog box appear.
        """

        # Instantiate page objects
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoProgressBarPage = demoPage.gotoProgressBar()

        demoProgressBarPage.click_random_progress_bar_tab()

        demoProgressBarPage.click_random_color_button()

        demoProgressBarPage.print_progress_bar_info()

        demoProgressBarPage.click_indeterminate_button()

        demoProgressBarPage.print_progress_bar_info()

        demoProgressBarPage.click_random_value_determinate_button()

        demoProgressBarPage.print_progress_bar_info()

    def test_download_click_opens_dialog(self):
        """
        Verifies that clicking the 'Start Download' button makes the
        file download dialog box appear.
        """

        # Instantiate page objects
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoProgressBarPage = demoPage.gotoProgressBar()


        # Step 2: Click the button that starts the download
        demoProgressBarPage.click_start_download_button()


        # Step 3: Assert that the download dialog is now present on the page
        assert demoProgressBarPage.is_download_dialog_present(), \
            "FAIL: The file download dialog did not appear after clicking 'Start Download'."

        time.sleep(3)


    def test_cancel_button_appears(self):
        """
        Verifies that clicking the 'Start Download' button makes the
        file download dialog box appear.
        """

        # Instantiate page objects
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoProgressBarPage = demoPage.gotoProgressBar()


        # Step 2: Click the button that starts the download
        demoProgressBarPage.click_start_download_button()


        # Step 3: Assert that the download dialog is now present on the page
        assert demoProgressBarPage.is_cancel_button_present(), \
            "FAIL: The cancel button does not appear when the download starts."

        time.sleep(3)

    def test_download_dialog_closes(self):
        """
        Verifies that clicking the 'Start Download' button makes the
        file download dialog box appear.
        """

        # Instantiate page objects
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoProgressBarPage = demoPage.gotoProgressBar()


        # Step 2: Click the button that starts the download
        demoProgressBarPage.click_start_download_button()

        # Step 3: Assert that the close button appears after download
        assert demoProgressBarPage.is_close_button_present(), \
            "FAIL: The Close button does not appear when download is complete"

        assert demoProgressBarPage.verify_dialog_closes_after_close_click(), \
            "FAIL: the dialog box is still active and did not close."

    def test_buttons_and_progress_bar_appear(self):
        """
        Verifies that clicking the 'Start Download' button makes the
        file download dialog box appear.
        """

        # Instantiate page objects
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoProgressBarPage = demoPage.gotoProgressBar()


        # Step 2: Click the button that starts the download
        demoProgressBarPage.click_start_download_button()

        assert demoProgressBarPage.is_downloading_box_present(), \
            "FAIL: The button does not say 'Downloading'"

        assert demoProgressBarPage.is_progress_bar_present(), \
            "FAIL: The progress bar has not appeared."


        # Step 3: Assert that the close button appears after download
        assert demoProgressBarPage.is_close_button_present(), \
            "FAIL: The Close button does not appear when download is complete"





