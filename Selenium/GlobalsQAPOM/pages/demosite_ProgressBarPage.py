from pages.BasePage import BasePage
from pages.Header_Components import HeaderComponent
from locators.demosite_progress_bar_page_locators import DemoProgressBarPageLocators
from selenium.common.exceptions import TimeoutException
import time
import pytest
import re

class DemoProgressBarPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.demoProgressBarPageLocators = DemoProgressBarPageLocators()

    def _click_tab(self, tab_locator: list):
        """
        Internal method to click on a tab.
        """
        self.logger.info(f"Clicking the tab with locator: {tab_locator}")
        self.element_click(tab_locator)

    def click_random_progress_bar_tab(self):
        self._click_tab(DemoProgressBarPageLocators.random_progress_bar_tab)

    def is_download_dialog_present(self) -> bool:
        """
        Checks if the 'empty recycle bin' dialog element is present on the page.
        This is a safe way to check for element existence without an exception.
        """
        self.logger.info("Checking for the presence of the 'empty recycle bin' element.")
        try:
            # Step 1: Switch to the iframe
            self.switch_to_frame(DemoProgressBarPageLocators.download_manager_demo_iframe)

            # Step 2: Look for the element inside the iframe
            self.wait_for_element_to_be_visible(DemoProgressBarPageLocators.downloading_dialog_locator, timeout=1)
            return True
        except:
            # If the element is not found within the timeout, return False
            return False
        finally:
            # Step 3: Always switch back to the default content
            self.switch_to_default_content()

    def is_cancel_button_present(self) -> bool:
        """
        Checks if the "Cancel" button is visible in the download dialog.
        This element is inside the message box iframe.
        """
        self.logger.info("Checking for the presence of the 'Cancel' button.")
        try:
            # Step 1: Switch to the iframe
            self.switch_to_frame(DemoProgressBarPageLocators.download_manager_demo_iframe)
            # Step 2: Look for the "Cancel" button element
            self.wait_for_element_to_be_visible(DemoProgressBarPageLocators.cancel_download_button_locator, timeout=2)
            return True
        except:
            # If the wait times out, the element is not visible
            return False
        finally:
            # Step 3: Always switch back to the default content
            self.switch_to_default_content()

    def is_downloading_box_present(self) -> bool:
        """
        Checks if the "Cancel" button is visible in the download dialog.
        This element is inside the message box iframe.
        """
        self.logger.info("Checking for the presence of the 'Cancel' button.")
        try:
            # Step 1: Switch to the iframe
            self.switch_to_frame(DemoProgressBarPageLocators.download_manager_demo_iframe)
            # Step 2: Look for the "Cancel" button element
            self.wait_for_element_to_be_visible(DemoProgressBarPageLocators.downloading_button_locator, timeout=4)
            return True
        except:
            # If the wait times out, the element is not visible
            return False
        finally:
            # Step 3: Always switch back to the default content
            self.switch_to_default_content()

    def is_progress_bar_present(self) -> bool:
        """
        Checks if the "Cancel" button is visible in the download dialog.
        This element is inside the message box iframe.
        """
        self.logger.info("Checking for the presence of the 'Progress Bar'")
        try:
            # Step 1: Switch to the iframe
            self.switch_to_frame(DemoProgressBarPageLocators.download_manager_demo_iframe)
            # Step 2: Look for the "Cancel" button element
            self.wait_for_element_to_be_visible(DemoProgressBarPageLocators.downloading_button_locator, timeout=4)
            return True
        except:
            # If the wait times out, the element is not visible
            return False
        finally:
            # Step 3: Always switch back to the default content
            self.switch_to_default_content()

    def is_close_button_present(self) -> bool:
        """
        Checks if the "Cancel" button is visible in the download dialog.
        This element is inside the message box iframe.
        """
        self.logger.info("Checking for the presence of the 'Cancel' button.")
        try:
            # Step 1: Switch to the iframe
            self.switch_to_frame(DemoProgressBarPageLocators.download_manager_demo_iframe)
            # Step 2: Look for the "Cancel" button element
            self.wait_for_element_to_be_visible(DemoProgressBarPageLocators.close_download_button_locator, timeout=12)
            return True
        except:
            # If the wait times out, the element is not visible
            return False
        finally:
            # Step 3: Always switch back to the default content
            self.switch_to_default_content()

    def click_start_download_button(self):
        """
        Clicks the 'Start Download' button, which triggers the dialog box.
        This element is inside the message box iframe.
        """
        try:
            self.logger.info("Clicking the 'Start Download' button.")
            # Step 1: Switch to the iframe
            self.switch_to_frame(DemoProgressBarPageLocators.download_manager_demo_iframe)
            # Step 2: Click the download button inside the iframe
            self.element_click(DemoProgressBarPageLocators.start_download_button_locator)
        finally:
            # Step 3: Always switch back to the default content
            self.switch_to_default_content()


    def close_file_download(self):
        try:
            self.logger.info("Clicking the 'Start Download' button.")
            # Step 1: Switch to the iframe
            self.switch_to_frame(DemoProgressBarPageLocators.download_manager_demo_iframe)
            # Step 2: Click the download button inside the iframe
            self.element_click(DemoProgressBarPageLocators.close_download_button_locator)
        finally:
            # Step 3: Always switch back to the default content
            self.switch_to_default_content()


    def verify_dialog_closes_after_close_click(self) -> bool:
        """
        Tests the full scenario: starts download, clicks close, and verifies the dialog is gone.
        This method combines other page object methods to create a full test case.
        """
        self.logger.info("Starting test to verify dialog closes after clicking 'Close'.")

        # Start the download process and open the dialog
        #self.click_start_download_button()

        # Wait for the dialog to appear and verify it is present
        if not self.is_download_dialog_present():
            self.logger.error("Download dialog was not present after clicking 'Start Download'. Test failed.")
            return False

        # Click the close button to dismiss the dialog
        self.close_file_download()

        # Verify that the dialog is no longer present
        if self.is_download_dialog_present():
            self.logger.error("Download dialog did not close after clicking 'Close'. Test failed.")
            return False

        self.logger.info("Successfully verified that the dialog box closes after clicking 'Close'. Test passed.")
        return True


    def click_random_value_determinate_button(self):
        """
        Clicks the 'Start Download' button, which triggers the dialog box.
        This element is inside the message box iframe.
        """
        try:
            self.logger.info("Clicking the 'Start Download' button.")
            # Step 1: Switch to the iframe
            self.switch_to_frame(DemoProgressBarPageLocators.random_progress_bar_demo_iframe)
            # Step 2: Click the download button inside the iframe
            self.element_click(DemoProgressBarPageLocators.random_value_determinate_button_locator)
        finally:
            # Step 3: Always switch back to the default content
            self.switch_to_default_content()

    def click_indeterminate_button(self):
        """
        Clicks the 'Start Download' button, which triggers the dialog box.
        This element is inside the message box iframe.
        """
        try:
            self.logger.info("Clicking the 'Start Download' button.")
            # Step 1: Switch to the iframe
            self.switch_to_frame(DemoProgressBarPageLocators.random_progress_bar_demo_iframe)
            # Step 2: Click the download button inside the iframe
            self.element_click(DemoProgressBarPageLocators.indeterminate_button_locator)
        finally:
            # Step 3: Always switch back to the default content
            self.switch_to_default_content()

    def click_random_color_button(self):
        """
        Clicks the 'Start Download' button, which triggers the dialog box.
        This element is inside the message box iframe.
        """
        try:
            self.logger.info("Clicking the 'Start Download' button.")
            # Step 1: Switch to the iframe
            self.switch_to_frame(DemoProgressBarPageLocators.random_progress_bar_demo_iframe)
            # Step 2: Click the download button inside the iframe
            self.element_click(DemoProgressBarPageLocators.random_color_button_locator)
        finally:
            # Step 3: Always switch back to the default content
            self.switch_to_default_content()

    def get_progress_bar_attributes(self) -> tuple[int, str]:
        """
        Retrieves the percentage and background color from the progress bar.

        Returns:
            A tuple containing the percentage as an integer and the background
            color as a string (e.g., (50, 'rgb(126, 225, 213)')).
            Returns (0, '') on failure.
        """
        self.logger.info("Attempting to get progress bar attributes.")

        percentage = 0
        background_color = ""

        try:
            # Step 1: Switch to the iframe
            self.switch_to_frame(DemoProgressBarPageLocators.random_progress_bar_demo_iframe)

            # Step 2: Use your get_element_attribute method to get the 'style' string
            style_attribute = self.get_element_attribute(DemoProgressBarPageLocators.random_progress_bar_locator, "style")

            # Step 3: Use regular expressions to extract the percentage and color
            percentage_match = re.search(r'width: (\d+)%;', style_attribute)
            if percentage_match:
                percentage = int(percentage_match.group(1))

            # Updated regex to correctly match rgba and rgb values
            color_match = re.search(r'background: (rgba?\([^)]+\));', style_attribute)
            if color_match:
                background_color = color_match.group(1)

            self.logger.info(f"Progress bar attributes found: Percentage={percentage}, Color={background_color}")

            return percentage, background_color

        except TimeoutException:
            self.logger.error("Progress bar element not found within the timeout.")
            return percentage, background_color

        finally:
            # Step 4: Always switch back to the default content
            self.switch_to_default_content()

    def print_progress_bar_info(self):
        """
        Calls get_progress_bar_attributes and prints the returned values.
        """
        self.logger.info("Retrieving and printing progress bar information.")

        # Get the percentage and color from the progress bar
        percentage, color = self.get_progress_bar_attributes()

        # Print the results
        print(f"Current Download Progress: {percentage}%")
        print(f"Progress Bar Background Color: {color}")


    def test_progress_bar_percentage_updates(self):
        """
        Tests that the progress bar's percentage updates after clicking the
        'percentage update' button.
        """
        self.logger.info("Starting test to verify percentage updates.")

        # Step 1: Get the initial progress bar percentage
        initial_percent, _ = self.get_progress_bar_attributes()
        self.logger.info(f"Initial progress: {initial_percent}%")

        # Step 2: Click the button to update the percentage
        self.click_random_value_determinate_button()

        # Step 3: Wait for the percentage to change
        updated_percent = initial_percent
        timeout = 10
        start_time = time.time()

        while updated_percent == initial_percent and (time.time() - start_time) < timeout:
            updated_percent, _ = self.get_progress_bar_attributes()
            time.sleep(0.5)

        # Step 4: Get the final, updated percentage
        updated_percent, _ = self.get_progress_bar_attributes()
        self.logger.info(f"Updated progress: {updated_percent}%")

        # Step 5: Assert that the percentage has increased
        assert updated_percent != initial_percent, "FAIL: The progress bar percentage did not change."

        self.logger.info("Test Passed: Progress bar percentage updated successfully.")
        return True

    def test_progress_bar_color_updates(self):
        """
        Tests that the progress bar's color updates after clicking the
        'color update' button.
        """
        self.logger.info("Starting test to verify color updates.")

        # Step 1: Get the initial progress bar color
        _, initial_color = self.get_progress_bar_attributes()
        self.logger.info(f"Initial color: {initial_color}")

        # Step 2: Click the button to update the color
        self.click_random_color_button()

        # Step 3: Wait for the color to change
        updated_color = initial_color
        timeout = 10
        start_time = time.time()

        while updated_color == initial_color and (time.time() - start_time) < timeout:
            _, updated_color = self.get_progress_bar_attributes()
            time.sleep(0.5)

        # Step 4: Get the final, updated color
        _, updated_color = self.get_progress_bar_attributes()
        self.logger.info(f"Updated color: {updated_color}")

        # Step 5: Assert that the color has changed
        assert updated_color != initial_color, "FAIL: The progress bar background color did not change."

        self.logger.info("Test Passed: Progress bar color updated successfully.")
        return True
