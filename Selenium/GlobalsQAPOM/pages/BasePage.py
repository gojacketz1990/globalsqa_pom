import logging
from utilities.LoggerBase import LoggerBase
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException, NoAlertPresentException
import requests
import random
import time
import json

# Basic logging configuration to output to the console
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class BasePage(LoggerBase):
    """
    A base class for all Page Objects.
    Contains common methods for interacting with web elements,
    using a self-healing locator pattern and explicit waits.
    """
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = self.getLogger()

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


    def scroll_to_element(self, locators):
        """Scrolls the element into the center of the viewport."""
        element = self.get_element(locators)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def _get_by_method(self, locator_type):
        """Retrieve the Selenium By method for a given locator type.
        Requires a locator_type which is a list of one or more tuples in the form:
        username_locator = [
        ("name", "user-name"),
        ("id", "user-name"),
        ("xpath", "//input[@placeholder='Username']")
        ]
        Returns the dictionary from the locator type
        Is not called directly but by other methods
        """
        if locator_type not in self.LOCATOR_DICT:
            raise ValueError(f"Invalid locator type: {locator_type}. Valid types are: {list(self.LOCATOR_DICT.keys())}")
        return self.LOCATOR_DICT[locator_type]

    def _find_element_with_wait(self, locators, expected_condition, timeout=None):
        """
        Private helper method to find a single element using a given ExpectedCondition.
        It uses a custom timeout if provided, otherwise, it uses the default wait object.
        Iterates through the locator list of tuples until it find the element or runs out of locators and
        returns a NoSuchElementException
        """
        wait = WebDriverWait(self.driver, timeout) if timeout else self.wait
        for locator_type, locator_value in locators:
            try:
                by_method = self._get_by_method(locator_type)
                return wait.until(expected_condition((by_method, locator_value)))
            except (NoSuchElementException, TimeoutException):
                self.logger.info(f"Locator failed: {locator_type}={locator_value}. Retrying with next locator.")
                continue
        raise NoSuchElementException(f"Element not found using any of the provided locators: {locators}")

    def _find_elements_with_wait(self, parent_element, locators, timeout=None):
        """
        Not directly callable, called by other methods
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



    def get_element(self, locators):
        """Find a single web element using self-healing locators."""
        return self._find_element_with_wait(locators, EC.presence_of_element_located)


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

    def is_element_present(self, locators):
        """Checks if a web element is present."""
        try:
            self.get_element(locators)
            return True
        except NoSuchElementException:
            return False

    def is_element_selected(self, locators):
        """
        Checks if an element is selected (e.g., radio button, checkbox).

        Args:
            locators (list): A list of locator tuples for the element.

        Returns:
            bool: True if the element is selected, False otherwise.
        """
        try:
            element = self.get_element(locators)
            return element.is_selected()
        except NoSuchElementException:
            self.logger.warning(f"Element not found, cannot check if selected: {locators}")
            return False

    def select_from_dropdown_by_visible_text(self, locators, text):
        """Select from a dropdown list by text using self-healing locators."""
        element = self.get_element(locators)
        select = Select(element)
        select.select_by_visible_text(text)

    def get_dropdown_selected_option_text(self, locators):
        """Retrieves the text of the currently selected option from a dropdown."""
        element = self.get_element(locators)
        select = Select(element)
        return select.first_selected_option.text

    def select_random_in_dropdown(self, locators):
        """Select a random option from a dropdown list, excluding the first option."""
        dropdown_element = self.get_element(locators)
        dropdown = Select(dropdown_element)
        options = dropdown.options[1:]
        if options:
            random_option = random.choice(options)
            dropdown.select_by_visible_text(random_option.text)

    def select_from_dropdown_by_value(self, locators: list, value: str):
        """
        Selects an option from a dropdown list by its 'value' attribute
        using self-healing locators.

        Args:
            locators (list): A list of locator tuples for the dropdown element.
            value (str): The 'value' attribute of the option to select.
        """
        self.logger.info(f"Attempting to select dropdown option with value: '{value}'.")
        element = self.get_element(locators) # Get the <select> element
        select = Select(element)
        select.select_by_value(value)
        self.logger.info(f"Selected dropdown option with value '{value}'.")

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

    # def get_element_attribute(self, locators, attribute):
    #     """Get a web element's attribute value."""
    #     element = self.get_element(locators)
    #     return element.get_attribute(attribute)
    #
    def get_element_attribute(self, locator: tuple, attribute: str) -> str:
        """
        Retrieves the value of a specified attribute from an element.
        """
        self.logger.info(f"Getting attribute '{attribute}' for element with locator {locator}.")
        try:
            element: WebElement = self.wait.until(EC.presence_of_element_located(locator))
            return element.get_attribute(attribute)
        except TimeoutException:
            self.logger.error(f"Element with locator {locator} not found within the timeout period.")
            return ""
        except Exception as e:
            self.logger.error(f"Failed to get attribute '{attribute}': {e}")
            return ""

    def get_element_css_property(self, locators, property_name: str) -> str:
        """
        Retrieves a CSS property value of a web element.

        Args:
            locators (list): A list of locator tuples for the element.
            property_name (str): The name of the CSS property to retrieve (e.g., 'font-size').

        Returns:
            str: The value of the CSS property.
        """
        self.logger.info(f"Retrieving CSS property '{property_name}' for element with locators: {locators}")
        element = self.get_element(locators)
        return element.value_of_css_property(property_name)

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

#This is a powerful item that we can leverage:

    # def get_dynamic_locator(self, locators: list, value: str):
    #     """
    #     Formats a dynamic locator with a given value.
    #
    #     Args:
    #         locators (list): A list of locator tuples with a placeholder.
    #         value (str): The value to insert into the locator's placeholder.
    #
    #     Returns:
    #         list: A new list of locator tuples with the formatted locator value.
    #     """
    #     formatted_locators = []
    #     for locator_type, locator_value in locators:
    #         formatted_locator = locator_value.format(value)
    #         formatted_locators.append((locator_type, formatted_locator))
    #    return formatted_locators


    def get_dynamic_locator(self, locators: list, value: str):
        return [(loc_type, loc_value.format(value)) for loc_type, loc_value in locators]

    def get_dynamic_locator_multiple(self, locators: list, *args):
        """
        Formats a dynamic locator with a variable number of values.

        Args:
            locators (list): A list of locator tuples with placeholders.
            *args: The values to insert into the locator's placeholders.

        Returns:
            list: A new list of locator tuples with the formatted locator value.
        """
        formatted_locators = []
        for locator_type, locator_value in locators:
            formatted_locator = locator_value.format(*args)
            formatted_locators.append((locator_type, formatted_locator))
        return formatted_locators

    def switch_to_window_by_title(self, title):
        """Switch to a window by its title."""
        self.wait.until(lambda d: len(d.window_handles) > 1)
        windows = self.driver.window_handles
        for window in windows:
            self.driver.switch_to.window(window)
            if self.driver.title == title:
                break

    def switch_to_alert_and_accept_popup(self):
        """Switches to an alert popup and accepts it."""
        try:
            alert = self.wait.until(EC.alert_is_present())
            self.logger.info(f"Alert text: {alert.text}")
            alert.accept()
        except (TimeoutException, NoAlertPresentException):
            self.logger.warning("No alert was present to accept.")
            raise

    def dismiss_all_alerts(self, timeout=2):
        """
        Dismisses all alert popups one after another.
        This method will keep trying to accept alerts until no more appear
        within a short timeout.

        Args:
            timeout (int): The maximum time to wait for a subsequent alert.
        """
        while True:
            time.sleep(2)
            try:
                # Use a very short wait to quickly check for the next alert
                alert = WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
                self.logger.info(f"Dismissing alert with text: '{alert.text}'")
                alert.accept()
            except (TimeoutException, NoAlertPresentException):
                self.logger.info("No more alerts found.")
                break # Exit the loop when no alert is present

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


    def set_slider_to_value(self, slider_element, handle_element, target_value, min_value, max_value):
        slider_width = self.driver.execute_script("return arguments[0].offsetWidth;", slider_element)
        range = max_value - min_value
        if not (min_value <= target_value <= max_value):
            raise ValueError(f"Value {target_value} out of range {min_value}–{max_value}")

        relative_pos = (target_value - min_value) / range
        target_x = slider_width * relative_pos

        # Current position of handle (left style %)
        current_left = float(self.driver.execute_script("return arguments[0].style.left;", handle_element).replace('%','') or 0)
        current_x = slider_width * current_left / 100

        offset = target_x - current_x

        actions = ActionChains(self.driver)
        actions.move_to_element(handle_element).click_and_hold().move_by_offset(offset, 0).release().perform()


    def drag_element_by_offset(self, element, offset_x, offset_y=0):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().move_by_offset(offset_x, offset_y).release().perform()

    def drag_element_not_center(self, element, offset_x, offset_y=0):
        actions = ActionChains(self.driver)
        actions.click_and_hold(element)
        actions.move_by_offset(offset_x, offset_y)
        actions.release()
        actions.perform()


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

    def wait_for_all_elements_to_be_visible(self, locators, timeout=None):
        """Wait for all elements to become visible."""
        wait_obj = WebDriverWait(self.driver, timeout) if timeout else self.wait
        for locator_type, locator_value in locators:
            try:
                by_method = self._get_by_method(locator_type)
                return wait_obj.until(EC.visibility_of_all_elements_located((by_method, locator_value)))
            except (NoSuchElementException, TimeoutException):
                self.logger.info(f"Locator failed: {locator_type}={locator_value}. Retrying with next locator.")
                continue
        raise NoSuchElementException(f"Elements not found using any of the provided locators: {locators}")


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



    def multiselect_items_by_text(self, items_locator: tuple, item_texts: list):
        """
        Multiselects a list of items by their text using Ctrl + click.
        This method assumes the driver is already in the correct context (e.g., inside an iframe).

        Args:
            items_locator (tuple): A locator tuple that points to all the selectable items
                                   (e.g., (By.CSS_SELECTOR, "#selectable li")).
            item_texts (list): A list of strings, where each string is the exact text
                              of an item to be selected.

        Raises:
            NoSuchElementException: If any of the specified items are not found.
        """
        self.logger.info(f"Attempting to multiselect items with texts: {item_texts}.")

        # Get all the selectable elements in a single call for efficiency.
        all_selectable_items = self.get_elements(items_locator)
        if not all_selectable_items:
            raise NoSuchElementException(f"No elements found with locator {items_locator}.")

        # Find the elements that match the requested text.
        elements_to_select = [
            item for item in all_selectable_items if item.text in item_texts
        ]

        if not elements_to_select:
            raise NoSuchElementException(f"None of the requested items ({item_texts}) were found.")

        # Check if all requested items were found before proceeding.
        if len(elements_to_select) != len(item_texts):
            found_texts = {item.text for item in elements_to_select}
            not_found_texts = [text for text in item_texts if text not in found_texts]
            raise NoSuchElementException(f"The following requested items were not found: {not_found_texts}")

        actions = ActionChains(self.driver)

        # Iterate through the filtered list of elements and build the action chain.
        # This is more direct and less error-prone than iterating through all items.
        actions.key_down(Keys.COMMAND)
        for element in elements_to_select:
            actions.click(element)
            self.logger.info(f"Action added: Ctrl + click on item '{element.text}'.")

        actions.key_up(Keys.COMMAND)

        # Execute the entire chain of actions at once.
        actions.perform()
        self.logger.info("Successfully executed multiselect action.")


    def click_and_drag_elements(self, start_element, end_element):
        """
        Performs a click-and-drag action from a start element to an end element.
        This method is a generic, reusable function for any drag-and-drop action.

        Args:
            start_element: The starting WebElement for the drag.
            end_element: The ending WebElement for the drop.
        """
        try:
            self.logger.info("Attempting a click-and-drag action.")
            action_chains = ActionChains(self.driver)
            action_chains.click_and_hold(start_element) \
                         .pause(0.5) \
                         .move_to_element(end_element) \
                         .pause(0.5) \
                         .release() \
                         .perform()
            self.logger.info("Successfully performed click and drag action.")
        except Exception as e:
            self.logger.error(f"Failed to perform click and drag action: {e}")
            raise # Re-raise the exception to be handled by the calling method.





    def find_element_by_text(self, items_locator: tuple, item_text: str):
            """
            Finds a single element from a collection based on its exact text.

            Args:
                items_locator (tuple): A locator that points to all potential items.
                item_text (str): The exact text of the item to find.

            Returns:
                WebElement: The found element.

            Raises:
                NoSuchElementException: If the element with the specified text is not found.
            """
            all_items = self.get_elements(items_locator)
            for item in all_items:
                element_text = item.get_attribute('innerText').strip()
                #print(f"item.text is '{element_text}'")
                if element_text == item_text:
                    self.logger.info(f"Found element with text '{element_text}'.")
                    return item

            raise NoSuchElementException(f"Could not find element with text '{item_text}'.")


    def select_all_text_in_element(self, locators):
        """
        Clicks an element and performs a 'Ctrl+A' action to select all text.

        Args:
            locators (list): A list of locator tuples for the element.
        """
        self.logger.info(f"Attempting to select all text in element with locators: {locators}")
        element = self.get_element_clickable(locators)

        actions = ActionChains(self.driver)
        actions.click(element)

        # Check for macOS to use Command key
        # if self.is_mac(): # You would need to implement this helper method
        actions.key_down(Keys.COMMAND).send_keys("a").key_up(Keys.COMMAND)
        # else:
        #     actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL)

        actions.perform()
        self.logger.info("Successfully performed 'Ctrl+A' action.")


    def upload_file(self, locators: list, file_path: str):
        """
        Uploads a file by sending its absolute path to a file input element.

        Args:
            locators (list): A list of locator tuples for the file input element.
            file_path (str): The relative or absolute path of the file to upload.
        """
        self.logger.info(f"Attempting to upload file at '{file_path}' to element with locators: {locators}")
        try:
            element = self.get_element(locators)
            element.send_keys(file_path)
            self.logger.info(f"Successfully uploaded file from path: {file_path}")
        except Exception as e:
            self.logger.error(f"Failed to upload file to element with locators {locators}. Error: {e}")
            raise # Re-raise the exception to be handled by the calling method.
    def get_element_text(self, locators: list) -> str:
        """
        Retrieves the text from an element after waiting for its presence.

        Args:
            locators (list): A list of locator tuples.

        Returns:
            str: The visible text of the element.
        """
        element = self.get_element(locators)
        return element.text

    def get_element_text(self, locators: list) -> str:
        """
        Retrieves the text from an element, cleaning it of non-breaking spaces.

        Args:
            locators (list): A list of locator tuples.

        Returns:
            str: The visible text of the element.
        """
        element = self.get_element(locators)

        return element.text.replace('\u00a0', '').strip()

    def get_json_data_from_element(self, locators, timeout=10):
        """
        Retrieves and parses JSON data from a web element.

        Args:
            locators (list): A list of locator tuples for the element containing the JSON.
            timeout (int): The maximum time to wait for the element.

        Returns:
            dict: The parsed JSON data as a dictionary.

        Raises:
            ValueError: If the text is not valid JSON.
            NoSuchElementException: If the element is not found.
        """
        self.logger.info(f"Attempting to retrieve JSON from locators: {locators}")
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.presence_of_element_located((By.XPATH, locators[0][1])))

            json_text = element.text.strip()
            if not json_text:
                raise ValueError("Element text is empty, cannot parse JSON.")

            return json.loads(json_text)

        except TimeoutException:
            self.logger.error(f"Element with JSON not found after {timeout} seconds.")
            raise
        except json.JSONDecodeError as e:
            self.logger.error(f"Failed to decode JSON from element text. Error: {e}")
            raise ValueError("The element's text is not valid JSON.")

    def is_text_present_in_element(self, locators: list, text_to_verify: str) -> bool:
        """
        Checks if a specific text is present within an element found by locators.

        Args:
            locators (list): The locator tuples to find the element.
            text_to_verify (str): The text to search for.

        Returns:
            bool: True if the text is found, False otherwise.
        """
        try:
            element = self.get_element(locators)
            # Check the element's visible text
            if text_to_verify in element.text:
                self.logger.info(f"Text '{text_to_verify}' found in element located by {locators}.")
                return True
            else:
                self.logger.info(f"Text '{text_to_verify}' NOT found. Element text was '{element.text}'.")
                return False
        except NoSuchElementException:
            self.logger.warning(f"Element not found using locators: {locators}. Cannot verify text.")
            return False

    def find_child_element_by_text(self, parent_element: WebElement, text_to_verify: str) -> WebElement:
        """
        Finds a child element by its exact text within a parent element.

        Args:
            parent_element (WebElement): The element to search within.
            text_to_verify (str): The text to search for.

        Returns:
            WebElement: The found child element.

        Raises:
            NoSuchElementException: If the element is not found.
        """
        return parent_element.find_element(By.XPATH, f".//*[normalize-space(.)='{text_to_verify}']")


    def get_element_text_content(self, locator: tuple) -> str:
        """
        Retrieves an element's text content, whether visible or not.
        This is useful for getting text from hidden elements or those styled with CSS that
        prevents .text from working.
        """
        try:
            # Wait for the element to be present in the DOM
            element = self.wait.until(EC.presence_of_element_located(locator))

            # Get the text content using the 'textContent' attribute
            text_content = element.get_attribute("textContent")

            # Log the action for debugging purposes
            self.logger.info(f"Retrieved text content from element with locator {locator}: '{text_content}'")

            return text_content.strip()  # .strip() removes leading/trailing whitespace

        except TimeoutException:
            self.logger.error(f"Element with locator {locator} not found within the timeout period.")
            return ""
        except Exception as e:
            self.logger.error(f"Failed to get text content for element with locator {locator}: {e}")
            return ""