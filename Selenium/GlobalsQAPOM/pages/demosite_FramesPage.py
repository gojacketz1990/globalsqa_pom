from pages.BasePage import BasePage
from pages.Header_Components import HeaderComponent
from locators.demosite_frames_page_locator import DemoFramesPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import pytest

class DemoFramesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.demoFramesPageLocators = DemoFramesPageLocators()

    def _click_tab(self, tab_locator: list):
        """
        Internal method to click on a tab.
        """
        self.logger.info(f"Clicking the tab with locator: {tab_locator}")
        self.element_click(tab_locator)

    def click_open_new_bowser_tab_button(self):

        try:
            self.logger.info("Clicking the 'Click Here' button.")
            # Step 1: Switch to the iframe
            #self.switch_to_frame(DemoFramesPageLocators.click_here_button)
            # Step 2: Click the download button inside the iframe
            self.element_click(DemoFramesPageLocators.click_here_button)
        finally:
            # Step 3: Always switch back to the default content
            self.switch_to_default_content()


    def verify_new_browser_tab_opens(self) -> bool:
        """
        Verifies that a new tab opens after clicking the 'Click Here' button
        and switches to it.

        Returns:
            True if a new tab is successfully opened and switched to, False otherwise.
        """
        try:
            # Step 1: Get the handles of all currently open windows/tabs before the click.
            # We get a list of handles to use for comparison.
            original_handles = self.driver.window_handles

            self.logger.info("Current number of window handles: %d", len(original_handles))

            # Step 2: Click the button that opens a new tab.
            self.click_open_new_bowser_tab_button()

            # Step 3: Wait for a new window to appear.
            # This is the corrected and more reliable way to wait. We tell it to
            # wait until the total number of windows is exactly one more than it was
            # before the click.
            self.logger.info("Waiting for a new tab to open.")
            WebDriverWait(self.driver, 10).until(
                EC.number_of_windows_to_be(len(original_handles) + 1)
            )

            # Step 4: Get all window handles again after the new window has opened.
            all_handles = self.driver.window_handles
            self.logger.info("New number of window handles: %d", len(all_handles))

            # Step 5: Find the new handle using a set difference for a clean solution.
            # Convert the lists to sets and find the handle that's in the new set
            # but not in the old one.
            new_tab_handle = (set(all_handles) - set(original_handles)).pop()

            # Step 6: Switch to the new tab.
            self.driver.switch_to.window(new_tab_handle)
            self.logger.info("Successfully switched to the new tab.")
            return True

        except TimeoutException:
            self.logger.error("Timeout: New tab did not open within the expected time.")
            return False

        except Exception as e:
            self.logger.error(f"An error occurred: {e}")
            return False


    def click_open_new_browsertab_tab(self):
        self._click_tab(DemoFramesPageLocators.open_new_browser_tab_locator)


    def click_open_new_browserwindow_tab(self):
        self._click_tab(DemoFramesPageLocators.open_new_window_tab_locator)


    def click_iframe_tab(self):
        self._click_tab(DemoFramesPageLocators.iframe_tab_locator)

    def switch_to_globalsqa_iframe(self):
        self.switch_to_frame(DemoFramesPageLocators.globalsqa_iframe_locator)


    def test_click_link_in_iframe(self) -> bool:
        """
        Test case to demonstrate how to interact with a link inside an iframe.
        This test assumes the main page has an iframe and the iframe itself
        contains a link that, when clicked, changes text on the page.

        Returns:
            bool: True if the verification is successful, False otherwise.
        """
        try:
            # 1. Wait for the iframe to be present and switch to it.
            # It's best practice to wait for the iframe to be available.
            # You can locate the iframe by its ID, name, or a WebElement.
            # In this example, we'll use a CSS selector.
            self.switch_to_frame(DemoFramesPageLocators.globalsqa_iframe_locator)
            print("Successfully switched to the iframe.")

            # 2. Now that you're inside the iframe's context, you can locate and click the link.
            # Replace "link-id" with the actual locator for the link inside the iframe.
            self.element_click(DemoFramesPageLocators.loadrunner_training_link_locator)
            print("Clicked the link inside the iframe.")
            time.sleep(5)

            # 3. Verify the expected outcome.
            # For example, let's verify some new text appears after the click.
            verified_heading = self.get_element(DemoFramesPageLocators.heading_in_iframe)
            print(verified_heading.text)

            # 4. Check the condition and return a boolean.
            if "HP LoadRunner Training" in verified_heading.text:
                print("Verification successful: 'HP LoadRunner Training!' heading is present.")
                return True
            else:
                print("Verification failed: 'HP LoadRunner Training!' heading was not found.")
                return False

        except (TimeoutException, NoSuchElementException) as e:
            # Catch multiple exceptions that indicate a failure to find an element
            print(f"An error occurred: {e}. Could not find the element.")
            # Return False to indicate the test did not pass
            return False
        finally:
            # 5. VERY IMPORTANT: Switch back to the main document.
            # This allows you to interact with elements outside the iframe again.
            self.switch_to_default_content()
            print("Switched back to the main document.")

