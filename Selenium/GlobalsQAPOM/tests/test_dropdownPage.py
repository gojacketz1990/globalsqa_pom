

import pytest
from pages.globalsqa_mainpage import GlobalsqaMainPage
import time
from utilities.LoggerBase import LoggerBase

@pytest.mark.usefixtures("setup_globalsqa")
class TestDropdown(LoggerBase):

    def test_country_dropdown_opens(self):
        # Instantiate page objects
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoDropDownPage = demoPage.gotoDropdown()

        demoDropDownPage.click_dropdownown()

        time.sleep(4)

        expected_option = "Albania"

        is_present = demoDropDownPage.is_option_present(expected_option)

        assert is_present, f"Expected to find option '{expected_option}' but it was not present."



    def test_verify_select_country(self):
        """
        Verifies that clicking the 'Start Download' button makes the
        file download dialog box appear.
        """

        # Instantiate page objects
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoDropDownPage = demoPage.gotoDropdown()

        demoDropDownPage.select_country_from_dropdown("Austria")
        time.sleep(4)

        # Step 2: Get the text of the currently selected option.
        selected_country = demoDropDownPage.get_selected_country_text()

        # Step 3: Assert that the selected country is "Austria".
        assert selected_country == "Austria", f"Expected 'Austria' but found '{selected_country}'."


    def test_country_dropdown_is_visible(self):
        # Instantiate page objects
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoDropDownPage = demoPage.gotoDropdown()

        assert demoDropDownPage.is_dropdown_visible(), "Dropdown element is not visible on the page."


    def test_verify_select_country_changes(self):
        """
        Verifies that clicking the 'Start Download' button makes the
        file download dialog box appear.
        """

        # Instantiate page objects
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoDropDownPage = demoPage.gotoDropdown()

        selected_option = "Austria"

        demoDropDownPage.select_country_from_dropdown(selected_option)
        time.sleep(4)

        # Step 2: Get the text of the currently selected option.
        selected_country = demoDropDownPage.get_selected_country_text()

        # Step 3: Assert that the selected country is "Austria".
        assert selected_country == selected_option, f"Expected 'Austria' but found '{selected_country}'."


        selected_option = "Bermuda"

        demoDropDownPage.select_country_from_dropdown(selected_option)
        time.sleep(4)

        # Step 2: Get the text of the currently selected option.
        selected_country = demoDropDownPage.get_selected_country_text()

        # Step 3: Assert that the selected country is "Austria".
        assert selected_country == selected_option, f"Expected 'Austria' but found '{selected_country}'."

