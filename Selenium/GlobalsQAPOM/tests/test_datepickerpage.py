import pytest
from pages.globalsqa_mainpage import GlobalsqaMainPage
import time

@pytest.mark.usefixtures("setup_globalsqa")
class TestDatePicker:

    def test_simple_date_picker(self):
        """
        Verifies that clicking the 'Start Download' button makes the
        file download dialog box appear.
        """        # Instantiate page objects
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoDatePickerPage = demoPage.gotoDatePicker()


        demoDatePickerPage.click_date_picker_tab()

        demoDatePickerPage.click_simple_date_textbox()

        #
        #
        time.sleep(2)
        # demoDatePickerPage.click_icon_trigger_tab()
        # time.sleep(2)
        # demoDatePickerPage.click_dropdown_datepicker_tab()
        # time.sleep(1)
    # Use the method to select a date

        date = "12/15/2025"

        demoDatePickerPage.select_simple_date(date)
        time.sleep(2)
        # You can then add assertions to verify the date was set correctly
        # For example, by checking the text of the input field.
        # Note: This is an example, you might need a method to get the input value.
        value = demoDatePickerPage.get_selected_date_simple_from_input()
        assert value == date




    def test_dropdown_datepicker(self):
        """
        Verifies that clicking the 'Start Download' button makes the
        file download dialog box appear.
        """        # Instantiate page objects
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoDatePickerPage = demoPage.gotoDatePicker()

        demoDatePickerPage.click_dropdown_datepicker_tab()


        demoDatePickerPage.click_dropdown_datepicker_date_textbox()


        #
        #
        time.sleep(2)
        # demoDatePickerPage.click_icon_trigger_tab()
        # time.sleep(2)
        # demoDatePickerPage.click_dropdown_datepicker_tab()
        # time.sleep(1)
    # Use the method to select a date


        date = "12/15/2025"

        demoDatePickerPage.select_dropdown_datepicker_date(date)
        time.sleep(2)
        # You can then add assertions to verify the date was set correctly
        # For example, by checking the text of the input field.
        # Note: This is an example, you might need a method to get the input value.
        value = demoDatePickerPage.get_dropdown_datepicker_selected_date_from_input()
        assert value == date




    def test_icon_trigger(self):
        """
        Verifies that clicking the 'Start Download' button makes the
        file download dialog box appear.
        """        # Instantiate page objects
        """
        Verifies that clicking the 'Start Download' button makes the
        file download dialog box appear.
        """        # Instantiate page objects
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoDatePickerPage = demoPage.gotoDatePicker()


        demoDatePickerPage.click_date_picker_tab()

        demoDatePickerPage.click_icon_trigger_tab()

        demoDatePickerPage.click_icon_calendar()
        #
        time.sleep(2)
        # demoDatePickerPage.click_icon_trigger_tab()
        # time.sleep(2)
        # demoDatePickerPage.click_dropdown_datepicker_tab()
        # time.sleep(1)
    # Use the method to select a date

        date = "12/15/2025"

        demoDatePickerPage.select_icon_triggered_simple_date(date)
        time.sleep(2)
        # You can then add assertions to verify the date was set correctly
        # For example, by checking the text of the input field.
        # Note: This is an example, you might need a method to get the input value.
        value = demoDatePickerPage.get_icon_triggered_date_simple_from_input()
        assert value == date


