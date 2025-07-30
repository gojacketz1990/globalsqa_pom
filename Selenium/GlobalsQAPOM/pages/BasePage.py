import logging
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
import requests
import random
import time

# Basic logging configuration to output to the console
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class BasePage:
    """
    A base class for all Page Objects.
    Contains common methods for interacting with web elements,
    using a self-healing locator pattern and explicit waits.
    """
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = logging.getLogger(__name__)

    # Dictionary mapping locator types to Selenium's By attributes
    LOCATOR_DICT = {
        "id": By.ID,
        "name": By.NAME,
        "xpath": By.XPATH,
        "css": By.CSS_SELECTOR,
        "class_name": By.CLASS_NAME,
        "link_text": By.LINK_TEXT,
        "partial_link_text": By.PARTIAL_LINK_TEXT,
        "tag_name": By.TAG_NAME,
    }

    def _get_by_method(self, locator_type):
        """Retrieve the Selenium By method for a given locator type."""
        if locator_type not in self.LOCATOR_DICT:
            raise ValueError(f"Invalid locator type: {locator_type}. Valid types are: {list(self.LOCATOR_DICT.keys())}")
        return self.LOCATOR_DICT[locator_type]

    def _find_element_with_wait(self, locators, expected_condition, timeout=None):
        """
        Private helper method to find a single element using a given ExpectedCondition.
        It uses a custom timeout if provided, otherwise, it uses the default wait object.
        """
        wait_obj = WebDriverWait(self.driver, timeout) if timeout else self.wait
        for locator_type, locator_value in locators:
            try:
                by_method = self._get_by_method(locator_type)
                return wait_obj.until(expected_condition((by_method, locator_value)))
            except (NoSuchElementException, TimeoutException):
                self.logger.info(f"Locator failed: {locator_type}={locator_value}. Retrying with next locator.")
                continue
        raise NoSuchElementException(f"Element not found using any of the provided locators: {locators}")

    def _find_elements_with_wait(self, parent_element, locators, timeout=None):
        """
        Private helper method to find multiple elements using a given parent element as context.
        It uses a custom timeout if provided, otherwise, it uses the default wait object.
        """
        wait_obj = WebDriverWait(self.driver, timeout) if timeout else self.wait
        for locator_type, locator_value in locators:
            try:
                by_method = self._get_by_method(locator_type)
                return wait_obj.until(EC.presence_of_all_elements_located((by_method, locator_value)))
            except (NoSuchElementException, TimeoutException):
                self.logger.info(f"Locator failed: {locator_type}={locator_value}. Retrying with next locator.")
                continue
        raise NoSuchElementException(f"Elements not found using any of the provided locators: {locators}")

    def get_element(self, locators, timeout=None):
        """Find a single web element using self-healing locators."""
        return self._find_element_with_wait(locators, EC.presence_of_element_located, timeout)

    def get_element_clickable(self, locators, timeout=None):
        """Find a single web element that is clickable using self-healing locators."""
        return self._find_element_with_wait(locators, EC.element_to_be_clickable, timeout)

    def get_elements(self, locators, timeout=None):
        """Find multiple web elements using self-healing locators."""
        return self._find_elements_with_wait(self.driver, locators, timeout)

    def get_child_element(self, parent_element, locators, timeout=None):
        """
        Find a single child web element using self-healing locators given the input parent element.
        This method correctly uses a custom wait function to handle the parent element as the search context.
        """
        wait_obj = WebDriverWait(self.driver, timeout) if timeout else self.wait
        for locator_type, locator_value in locators:
            try:
                by_method = self._get_by_method(locator_type)
                # The lambda function is the key here. It tells the wait to look for the element
                # specifically within the parent_element's context.
                return wait_obj.until(lambda driver: parent_element.find_element(by_method, locator_value))
            except (NoSuchElementException, TimeoutException):
                self.logger.info(f"Child locator failed: {locator_type}={locator_value}. Retrying with next locator.")
                continue
        raise NoSuchElementException(f"Child element not found using any of the provided locators: {locators}")

    def get_child_elements(self, parent_element, locators, timeout=None):
        """Find child web elements using self-healing locators given the input parent element."""
        wait_obj = WebDriverWait(self.driver, timeout) if timeout else self.wait
        for locator_type, locator_value in locators:
            try:
                by_method = self._get_by_method(locator_type)
                return wait_obj.until(lambda driver: parent_element.find_elements(by_method, locator_value))
            except (NoSuchElementException, TimeoutException):
                self.logger.info(f"Child locator failed: {locator_type}={locator_value}. Retrying with next locator.")
                continue
        raise NoSuchElementException(f"Child elements not found using any of the provided locators: {locators}")

    def is_button_active(self, locators):
        """Check if a button is active based on its class attribute."""
        button = self.get_element(locators)
        button_class = button.get_attribute("class")
        return "active" in button_class

    def type_into_element(self, text, locators):
        """Type text into a web element."""
        element = self.get_element_clickable(locators)
        element.click()
        element.clear()
        element.send_keys(text)

    def type_into_element_clear_js(self, text, locators):
        """Clear an element with JavaScript and then type text."""
        element = self.get_element_clickable(locators)
        self.driver.execute_script("arguments[0].value = '';", element)
        element.send_keys(text)

    def send_keys_into_element(self, text, locators):
        """Type text into a web element without clearing."""
        element = self.get_element_clickable(locators)
        element.send_keys(text)

    def element_click(self, locators):
        """Click a web element found using self-healing locators with retries."""
        for _ in range(3):
            try:
                element = self.get_element_clickable(locators)
                element.click()
                return
            except StaleElementReferenceException:
                self.logger.info("Retrying click due to stale element.")
        raise StaleElementReferenceException(f"Failed to click element: {locators}")

    def retrieve_child_element_text(self, parent_element, locators):
        """Retrieve text from a child element given the parent element."""
        element = self.get_child_element(parent_element, locators)
        return element.text

    def retrieve_element_text(self, locators):
        """Retrieve text from a web element."""
        element = self.get_element(locators)
        return element.text

    def check_display_status_of_element(self, locators):
        """Check that a web element is displayed using self-healing locators."""
        element = self.get_element(locators)
        return element.is_displayed()

    def get_response_code(self, url):
        """Get a response code given a url."""
        try:
            response = requests.head(url, allow_redirects=True)
            return response.status_code
        except requests.RequestException as e:
            self.logger.error(f"Request exception: {e}")
            return None

    def wait_for_element_to_be_visible(self, locators, timeout=None):
        """Wait for an element to become visible."""
        return self._find_element_with_wait(locators, EC.visibility_of_element_located, timeout)

    def is_element_present(self, locators, timeout=5):
        """Checks if a web element is present."""
        try:
            self.get_element(locators, timeout)
            return True
        except NoSuchElementException:
            return False

    def select_from_dropdown_by_visible_text(self, locators, text):
        """Select from a dropdown list by text using self-healing locators."""
        element = self.get_element(locators)
        select = Select(element)
        select.select_by_visible_text(text)

    def select_random_in_dropdown(self, locators):
        """Select a random option from a dropdown list, excluding the first option."""
        dropdown_element = self.get_element(locators)
        dropdown = Select(dropdown_element)
        options = dropdown.options[1:]
        if options:
            random_option = random.choice(options)
            dropdown.select_by_visible_text(random_option.text)

    def hover_over_element(self, locators):
        """Hover over a web element using ActionChains using self-healing locators."""
        element = self.get_element(locators)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def hover_and_click_popup(self, hover_element_locator, click_element_locator):
        """Hover over an element and then click a subsequent popup element."""
        hover_element = self.get_element(hover_element_locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(hover_element).perform()
        popup_element = self.wait_for_element_to_be_visible(click_element_locator)
        popup_element.click()

    def switch_to_frame(self, iframe_locators, timeout=None):
            """Switch to an iframe given the iframe locator."""
            wait_obj = WebDriverWait(self.driver, timeout) if timeout else self.wait

            for locator_type, locator_value in iframe_locators:
                try:
                    by_method = self._get_by_method(locator_type)
                    # The expected condition needs a single locator tuple, not a list of them.
                    wait_obj.until(EC.frame_to_be_available_and_switch_to_it((by_method, locator_value)))
                    self.logger.info(f"Switched to iframe using locator: {locator_type}={locator_value}")
                    return # Exit the loop and method once a locator succeeds
                except (NoSuchElementException, TimeoutException):
                    self.logger.info(f"Locator failed to find iframe: {locator_type}={locator_value}. Retrying with next locator.")
                    continue # Try the next locator in the list

            # If the loop finishes without returning, none of the locators worked.
            self.logger.error(f"All locators failed to find the iframe: {iframe_locators}")
            raise NoSuchElementException(f"Error switching to iframe with any of the provided locators.")


    def switch_to_default_content(self):
        """Switch to default content."""
        self.driver.switch_to.default_content()

    def get_element_attribute(self, locators, attribute):
        """Get a web element's attribute value."""
        element = self.get_element(locators)
        return element.get_attribute(attribute)

    def scroll_into_center_view(self, locators):
        """Scroll the web element into the center of the visible view."""
        element = self.get_element(locators)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def verify_link_presence(self, text):
        """Verify that a link with the given text is present."""
        self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, text)))

    def get_auto_suggestive_items(self, locators):
        """Get a list of auto suggestive items."""
        items = self.get_elements(locators)
        return [item.text for item in items]

    def get_dynamic_locator(self, item_text):
        """Return a dynamic locator for an item based on its text."""
        return [("xpath", f"//div[text()='{item_text}']")]

    def switch_to_window_by_title(self, title):
        """Switch to a window by its title."""
        self.wait.until(lambda d: len(d.window_handles) > 1)
        windows = self.driver.window_handles
        for window in windows:
            self.driver.switch_to.window(window)
            if self.driver.title == title:
                break

    def switch_to_alert_and_accept_popup(self):
        """Switch to an alert popup and accept."""
        alert = self.wait.until(EC.alert_is_present())
        alert.accept()

    def read_table(self, table_locator, row_locator, cell_locator):
        """Return table data given the table, row, and cell locators."""
        table = self.get_element(table_locator)
        rows = self.get_child_elements(table, row_locator)
        table_data = []
        for row in rows:
            cells = self.get_child_elements(row, cell_locator)
            row_data = [cell.text for cell in cells]
            table_data.append(row_data)
        return table_data

    def read_table_with_th_row(self, table_locator, row_locator, cell_locators):
        """Return table data for cells with multiple data, given locators for `th` and `td`."""
        table = self.get_element(table_locator)
        rows = self.get_child_elements(table, row_locator)
        table_data = []
        for row in rows:
            row_data = []
            for cell_locator in cell_locators:
                cells = self.get_child_elements(row, [cell_locator])
                row_data.extend(cell.text.strip() for cell in cells)
            table_data.append(row_data)
        return table_data

    def check_checkbox(self, checkbox_locator, on_off):
        """Toggle checkbox On or Off given the checkbox locator."""
        checkbox = self.get_element(checkbox_locator)
        if on_off.upper() == "ON":
            if not checkbox.is_selected():
                checkbox.click()
        elif on_off.upper() == "OFF":
            if checkbox.is_selected():
                checkbox.click()

    def set_slider_value(self, slider_locator, value):
        """Locate slider and set the slider value given an input value."""
        slider = self.get_element(slider_locator)
        min_value = int(self.driver.execute_script("return arguments[0].min || '0';", slider))
        max_value = int(self.driver.execute_script("return arguments[0].max || '100';", slider))
        if not (min_value <= value <= max_value):
            raise ValueError(f"Value {value} is out of range. Must be between {min_value} and {max_value}.")
        value_to_set = min_value + ((max_value - min_value) * value / 100)
        self.driver.execute_script("arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('change'));", slider, value_to_set)

    def get_progress_bar_value(self, progress_bar_locator):
        """Return value of a progress bar."""
        progress_bar = self.get_element(progress_bar_locator)
        return progress_bar

    def get_shadow_root(self, host_locator):
        """Return shadow root."""
        host_element = self.get_element(host_locator)
        return self.driver.execute_script('return arguments[0].shadowRoot', host_element)

    def wait_for_shadow_child(self, shadow_root, child_locator_tuple, timeout=10):
        """
        Waits for a child element to appear inside a Shadow Root.
        """
        by_method, locator_value = child_locator_tuple
        end_time = time.time() + timeout
        while time.time() < end_time:
            try:
                element = shadow_root.find_element(by_method, locator_value)
                if element.is_displayed():
                    return element
            except NoSuchElementException:
                pass
            time.sleep(0.5)
        raise NoSuchElementException(f"Shadow child element not found after {timeout}s: {child_locator_tuple}")

    def click_shadow_child_element(self, host_locator, child_locator_tuple, timeout=10):
        """Click on a shadow child element given its host and a locator tuple."""
        shadow_root = self.get_shadow_root(host_locator)
        child_element = self.wait_for_shadow_child(shadow_root, child_locator_tuple, timeout)
        child_element.click()

    def find_text_on_page(self, text):
        """Searches for a given text anywhere on the page."""
        xpath = f"//*[contains(text(), '{text}')]"
        try:
            return self.wait.until(EC.presence_of_element_located((By.XPATH, xpath))).text
        except TimeoutException:
            return None

    def wait_for_attribute_value_to_be(self, locators, attribute, expected_value, timeout=None):
        """Wait for an element's attribute to have a specific value."""
        wait_obj = WebDriverWait(self.driver, timeout) if timeout else self.wait
        for locator_type, locator_value in locators:
            try:
                by_method = self._get_by_method(locator_type)
                wait_obj.until(
                    EC.text_to_be_present_in_element_attribute(
                        (by_method, locator_value),
                        attribute,
                        expected_value
                    )
                )
                self.logger.info(f"Attribute '{attribute}' has value '{expected_value}' for locator: {locator_type}={locator_value}")
                return True
            except (NoSuchElementException, TimeoutException):
                self.logger.info(f"Locator failed or condition not met: {locator_type}={locator_value}")
                continue
        self.logger.error(f"All locators failed to find element with attribute '{attribute}' having value '{expected_value}'.")
        return False

    def is_text_present(self, text):
        """Checks if a given text exists anywhere on the page."""
        return self.find_text_on_page(text) is not None

    def take_screenshot(self, filename):
        """Take a full page screenshot."""
        self.driver.save_screenshot('screenshots/' + filename)
        self.logger.info(f"Full page screenshot saved as {filename}")
