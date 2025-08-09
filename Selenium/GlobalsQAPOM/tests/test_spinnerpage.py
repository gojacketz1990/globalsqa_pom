import pytest
from pages.globalsqa_mainpage import GlobalsqaMainPage
import time

@pytest.mark.usefixtures("setup_globalsqa")
class TestSpinner:

    def test_select_currency(self):
        """
        Verifies that clicking the 'Start Download' button makes the
        file download dialog box appear.
        """

        # Instantiate page objects
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoSpinnerPage = demoPage.gotoSpinner()

        #demoSpinnerPage.click_simple_spinner_tab()
        #time.sleep(2)
        demoSpinnerPage.click_currency_tab()

        #Currency choices:  en-US, de-DE, ja-JP
        currency = "de-DE"

        demoSpinnerPage.select_currency_from_dropdown_by_value(currency)

        time.sleep(5)



    def test_spinner_value_retrieval(self):

           # Instantiate page objects
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoSpinnerPage = demoPage.gotoSpinner()

        #demoSpinnerPage.click_simple_spinner_tab()
        #time.sleep(2)
        demoSpinnerPage.click_currency_tab()

        current_value = demoSpinnerPage.get_current_spinner_value()
        print(f"The spinner's current value is: {current_value}")

        # Assert it's the expected initial value (e.g., 5)
        assert current_value == 5, f"Expected initial value to be 5, but got {current_value}"

    def test_spinner_value_change(self):
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoSpinnerPage = demoPage.gotoSpinner()

        #demoSpinnerPage.click_simple_spinner_tab()
        #time.sleep(2)
        demoSpinnerPage.click_currency_tab()
        current_value = demoSpinnerPage.get_current_spinner_value()
        print(f"Value after clicking down: {current_value}") # Should be 5 again

        # Click the up button
        demoSpinnerPage.click_spinner_button("up")
        demoSpinnerPage.click_spinner_button("up")
        demoSpinnerPage.click_spinner_button("up")
        current_value = demoSpinnerPage.get_current_spinner_value()
        print(f"Value after clicking up: {current_value}") # Should be 6 if starting at 5

        # Click the down button
        demoSpinnerPage.click_spinner_button("down")
        current_value = demoSpinnerPage.get_current_spinner_value()
        print(f"Value after clicking down: {current_value}") # Should be 5 again
        assert current_value == 55, f"Expected initial value to be 5, but got {current_value}"


    def test_upper_limit_amount(self):
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoSpinnerPage = demoPage.gotoSpinner()

        #demoSpinnerPage.click_simple_spinner_tab()
        #time.sleep(2)
        demoSpinnerPage.click_currency_tab()
        current_value = demoSpinnerPage.get_current_spinner_value()
        print(f"Value after clicking down: {current_value}") # Should be 5 again

        # Click the up button
        for i in range(100):
            demoSpinnerPage.click_spinner_button("up")

        current_value = demoSpinnerPage.get_current_spinner_value()
        print(f"Value after clicking up: {current_value}") # Should be 6 if starting at 5

        assert current_value == 2500, f"Expected initial value to be 5, but got {current_value}"


    def test_lower_limit_amount(self):
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoSpinnerPage = demoPage.gotoSpinner()

        #demoSpinnerPage.click_simple_spinner_tab()
        #time.sleep(2)
        demoSpinnerPage.click_currency_tab()
        current_value = demoSpinnerPage.get_current_spinner_value()
        print(f"Value after clicking down: {current_value}") # Should be 5 again

        # Click the up button
        for i in range(50):
            demoSpinnerPage.click_spinner_button("up")

        for j in range(100):
            demoSpinnerPage.click_spinner_button("down")

        current_value = demoSpinnerPage.get_current_spinner_value()
        print(f"Value after clicking up: {current_value}")

        assert current_value == 5, f"Expected initial value to be 5, but got {current_value}"

    def test_simple_spinner(self):
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoSpinnerPage = demoPage.gotoSpinner()

        #demoSpinnerPage.click_simple_spinner_tab()
        #time.sleep(2)
        demoSpinnerPage.click_simple_spinner_tab()

        for i in range(5):
            demoSpinnerPage.click_simple_spinner_button("up")

        current_value = demoSpinnerPage.get_current_simple_spinner_value()
        print(f"Value after clicking up: {current_value}")

        assert current_value == 5, f"Expected initial value to be 5, but got {current_value}"


        for j in range(3):
            demoSpinnerPage.click_simple_spinner_button("down")

        current_value = demoSpinnerPage.get_current_simple_spinner_value()
        print(f"Value after clicking up: {current_value}")

        assert current_value == 2, f"Expected initial value to be 2, but got {current_value}"

    def test_spinner_disables_on_toggle_click(self):
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoSpinnerPage = demoPage.gotoSpinner()

        #demoSpinnerPage.click_simple_spinner_tab()
        #time.sleep(2)
        demoSpinnerPage.click_simple_spinner_tab()


        # Step 1: Verify spinner is initially enabled (optional, but good practice)
        assert not demoSpinnerPage.is_spinner_input_disabled(), "Spinner input should be enabled initially."
        assert not demoSpinnerPage.are_spinner_buttons_disabled(), "Spinner buttons should be enabled initially."
        demoSpinnerPage.logger.info("Spinner confirmed to be enabled initially.")

        # Step 2: Click the toggle disable button
        demoSpinnerPage.toggle_disable_engage()

        # Add a small wait to allow the UI to update
        time.sleep(1)

        # Step 3: Verify the spinner input is now disabled
        assert demoSpinnerPage.is_spinner_input_disabled(), "FAIL: Spinner input did not become disabled."
        demoSpinnerPage.logger.info("Spinner input successfully verified as disabled.")

        # Step 4: Verify the spinner buttons are now disabled
        assert demoSpinnerPage.are_spinner_buttons_disabled(), "FAIL: Spinner buttons did not become disabled."
        demoSpinnerPage.logger.info("Spinner buttons successfully verified as disabled.")

        demoSpinnerPage.logger.info("✅ PASS: Spinner successfully disabled after toggle click.")

        #Enable them back

        demoSpinnerPage.toggle_disable_engage()

        # To verify the spinner is enabled:
        assert not demoSpinnerPage.is_spinner_input_disabled(), "FAIL: Spinner input should be enabled."
        assert not demoSpinnerPage.are_spinner_buttons_disabled(), "FAIL: Spinner buttons should be enabled."

