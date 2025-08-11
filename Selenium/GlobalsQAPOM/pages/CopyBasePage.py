from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
import requests
import random
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        #self.wait = WebDriverWait(driver, 8)

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

    def _find_element_with_wait(self, locators, expected_condition, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        for locator_type, locator_value in locators:
            try:
                by_method = self._get_by_method(locator_type)
                return wait.until(expected_condition((by_method, locator_value)))
            except (NoSuchElementException, TimeoutException):
                print(f"Locator failed: {locator_type}={locator_value}")
                continue
        raise NoSuchElementException(f"Element not found using any of the provided locators: {locators}")


    def get_element(self, locators):
        """Find a single web element using self-healing locators."""
        return self._find_element_with_wait(locators, EC.presence_of_element_located)


    def get_element_clickable(self, locators):
        """Find a single web element using self-healing locators in a React application."""
        wait = WebDriverWait(self.driver, 10)
        for locator_type, locator_value in locators:
            try:
                by_method = self._get_by_method(locator_type)

                # Wait for element presence to handle React re-renders
                wait.until(EC.presence_of_element_located((by_method, locator_value)))

                # Wait for the element to be clickable
                wait.until(EC.element_to_be_clickable((by_method, locator_value)))

                # Re-locate the element to ensure freshness
                return self.driver.find_element(by_method, locator_value)

            except (StaleElementReferenceException, TimeoutException):
                print(f"Retrying due to dynamic React updates: {locator_type}={locator_value}")
                continue

        raise NoSuchElementException(f"Element not found using any of the provided locators: {locators}")



    def get_elements(self, locators):
        """Find multiple web element using self-healing locators."""
        wait = WebDriverWait(self.driver,4)
        for locator_type, locator_value in locators:
            try:
                by_method = self._get_by_method(locator_type)
                elements = wait.until(EC.presence_of_all_elements_located((by_method, locator_value)))
                #print(f"Element found using locator: {locator_type}={locator_value}")
                return elements
            except (NoSuchElementException, TimeoutException):
                print(f"Locator failed: {locator_type}={locator_value}")
                continue

        raise NoSuchElementException(f"Element not found using any of the provided locators: {locators}")

    def get_child_element(self,parent_element, locators):
        """Find a single child web element using self-healing locators given the input parent element."""
        element = None
        wait = WebDriverWait(self.driver,10)
        for locator_type, locator_value in locators:
            try:
                by_method = self._get_by_method(locator_type)
                #print("get child element")
                #print(by_method)
                #print(locator_value)
                element = parent_element.find_element(by_method, locator_value)#There is not a good way to use get_element here so we manually
                #get the locator method and call find_element here
                #print(f"Element found using locator: {locator_type}={locator_value}")
                return element
            except (NoSuchElementException, TimeoutException):
                print(f"Locator failed: {locator_type}={locator_value}")
                continue

        raise NoSuchElementException(f"Element not found using any of the provided locators: {locators}")


    def get_child_elements(self,parent_element, locators):#This will mostly be used for tables
        """Find child web elements using self-healing locators given the input parent element."""
        element = None
        wait = WebDriverWait(self.driver,10)
        for locator_type, locator_value in locators:
            try:
                by_method = self._get_by_method(locator_type)
                elements = parent_element.find_elements(by_method, locator_value)
                #print(f"Element found using locator: {locator_type}={locator_value}")
                return elements
            except (NoSuchElementException, TimeoutException):
                print(f"Locator failed: {locator_type}={locator_value}")
                continue

        raise NoSuchElementException(f"Element not found using any of the provided locators: {locators}")

    def isButtonActive(self, locators):
        button = self.get_element(locators)
        button_class = button.get_attribute("class")  # Get the class attribute of the button
        if "active" in button_class:  # Check if "active" is in the class attribute
            print("The button is active.")
            return True  # Return True if the button is active
        else:
            print("The button is not active.")
            return False  # Return False if the button is not active


    def type_into_element(self, text, locators):
        """Type text into a web element found using self-healing locators."""

        element = self.get_element(locators)
        time.sleep(1)
        element.click()
        time.sleep(1)
        element.clear()
        element.send_keys(text)


    def type_into_element_clear(self, text, locators):
        """Clear a web element's text and type new text using self-healing locators.  Does this with javascript."""

        # Get the element using self-healing locators
        element = self.get_element(locators)

        # Clear the element using JavaScript
        self.driver.execute_script("arguments[0].value = '';", element)

        # Optionally click the element to focus
        element.click()

        # Type the new text into the element
        element.send_keys(text)

    def sendKeys_into_element(self, text, locators):
        """Type text into a web element found using self-healing locators."""
        element = self.get_element(locators)
        element.send_keys(text)

    def element_click(self, locators):
        """Click a web element found using self-healing locators."""
        for _ in range(10):  # Retry up to 3 times
            try:
                element = self.get_element_clickable(locators)
                element.click()
                return
            except StaleElementReferenceException:
                print("Retrying click due to stale element.")
        raise StaleElementReferenceException(f"Failed to click element: {locators}")

    def wait_presence_element(self, locators, timeout=10):#need to update this with try/except
        """Wait for an element to be present using self-healing locators."""
        wait = WebDriverWait(self.driver,timeout)
        for locator_type, locator_value in locators:

            by_method = self._get_by_method(locator_type)
            element = wait.until(
                EC.presence_of_element_located((by_method, locator_value))
            )
            #print(f"Element found using locator: {locator_type}={locator_value}")
            return element



    def retrieve_child_element_text(self,parent_element, locators):
        """Retrieve text from a child element given the parent element"""
        element = self.get_child_element(parent_element, locators)
        return element.text

    def wait_and_click_element(self, locators):
        """Click a web element after waiting for its visibility using self-healing locators."""
        wait = WebDriverWait(self.driver,10)
        for locator_type, locator_value in locators:
            try:
                by_method = self._get_by_method(locator_type)
                element = wait.until(
                    EC.presence_of_element_located((by_method, locator_value))
                )
                #print(f"Element found using locator: {locator_type}={locator_value}")
                element.click()
                return
            except (NoSuchElementException, TimeoutException):
                print(f"Locator failed: {locator_type}={locator_value}")
                continue

        raise NoSuchElementException(f"Element not found using any of the provided locators: {locators}")


    def element_child_click(self,parent_element, locators):
        """Click a child web element given the parent element found using self-healing locators."""
        element = self.get_child_element(parent_element, locators)
        element.click()

    def retrieve_element_text(self,locators):
        """Retrieve text from a web element"""
        element = self.get_element(locators)
        return element.text


    def check_display_status_of_element(self,locators):
        """Check that a web element is displayed using self-healing locators."""
        element = self.get_element(locators)
        return element.is_displayed()

    def get_response_code(self,url):
        """Get a response code given a url"""
        try:
            response = requests.head(url, allow_redirects=True)
            return response.status_code
        except requests.RequestException as e:
            print(f"Request exception: {e}")
            return None

    def wait_for_element_to_be_visible(self, locators):
        """Wait for an element to become visible"""
        wait = WebDriverWait(self.driver,10)
        for locator_type, locator_value in locators:
            try:
                by_method = self._get_by_method(locator_type)
                element = wait.until(
                    EC.visibility_of_element_located((by_method, locator_value))
                )
                print(f"Element found using locator: {locator_type}={locator_value}")
                return element
            except (NoSuchElementException, TimeoutException):
                print(f"Locator failed: {locator_type}={locator_value}")
                continue

        raise NoSuchElementException(f"Element not found using any of the provided locators: {locators}")

    def is_element_present(self, locators):
        """Check that a web element is present."""
        try:
            self.driver.get_element(locators)
            return True
        except:
            return False

    def select_from_dropdown_by_visible_text(self, locators, text):
        """Select from a dropdown list by text using self-healing locators."""
        element = self.get_element(locators)
        select = Select(element)
        select.select_by_visible_text(text)

    def select_random_in_dropdown(self, locators):
        """Select a random option from a dropdown list, excluding the first option."""
        dropdown_element = self.get_element(locators)  # Get the dropdown element
        dropdown = Select(dropdown_element)
        options = dropdown.options[1:]  # Exclude the first element by slicing
        if options:  # Ensure there are options to select
            random_option = random.choice(options)  # Randomly choose from remaining options
            dropdown.select_by_visible_text(random_option.text)

    def hover_over_element(self, locators):
        """Hover over a web element using ActionChains using self-healing locators."""
        element = self.get_element(locators)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def hover_and_click_popup(self,hover_element_locator, click_element_locator):
        """Hover over a web element using ActionChains then click a subsequent element using self-healing locators."""
        element = self.get_element(hover_element_locator)
        actions = ActionChains(self.driver)

        actions.move_to_element(element).perform()

        # Wait for the popup element to be visible
        popup_element = self.wait_for_element_to_be_visible(click_element_locator)

        # Click the popup element
        popup_element.click()

    def switch_to_frame(self, locators):
        """Switch to a frame"""
        frame = self.get_element(locators)
        self.driver.switch_to.frame(frame)

    def switch_to_default_content(self):
        """Switch to default content"""
        self.driver.switch_to.default_content()

    def get_element_attribute(self, locators, attribute):
        """get css element attributes"""
        element = self.get_element(locators)
        return element.get_attribute(attribute)

    def scroll_into_center_view(self, locators):
        """Scroll the web element into the center of the visible view"""
        element = self.get_element(locators)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        #element.click()

    def verifyLinkPresence(self,text): #Common method to find a link that exists and wait for it
        """Verify that link exists by Link Text"""
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.LINK_TEXT, text)))

    def get_auto_suggestive_items(self,locators):
        """Get a list of auto suggestive items"""
        items = self.get_elements(locators)
        return [item.text for item in items]

    def get_dynamic_locator(self, item_text):
        """Get an item using a dynamic locator text"""
        return [("xpath", f"//div[text()='{item_text}']")]

    def switch_to_window_by_title(self,title):
        """Switch to window by the title."""
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)

        # Get the window handles of all open windows
        windows = self.driver.window_handles
        original_window = self.driver.current_window_handle

        for window in windows:
            self.driver.switch_to.window(window)
            if self.driver.title == title:  # Replace with the title of the new window
                break

    def switch_to_alert_and_accept_popup(self):
        """Switch to an alert popup and accept"""
        alert = self.driver.switch_to.alert
        alert.accept()

    def read_table(self, table_locator, row_locator, cell_locator):
        """Return table data given the table locator, row locator and cell locators"""
        table = self.get_element(table_locator)
        rows = self.get_child_elements(table,row_locator)#we can create a custom find Child Elements for this or
        table_data = []

        for row in rows:
            cells =self.get_child_elements(row, cell_locator)
            row_data = [cell.text for cell in cells]
            table_data.append(row_data)

        return table_data


    def read_table_with_th_row(self, table_locator, row_locator, cell_locators):#this will make sure that is uses both cell locators
        #Some tables have a th row which is common and calls a different method in BasePage
        """Return table data given the table locator, row locator and cell locators.  For cells that have multiple data"""
        table = self.get_element(table_locator)
        rows = self.get_child_elements(table, row_locator)
        table_data = []

        for row in rows:
            row_data = []
            for cell_locator in cell_locators:#We are taking a list of tuples and pulling a single tuple but our methods require a list of tuples
                #so we need to take the single tuple and convert it back to a list of tuples - a list of one
                cell_locator_lt = [cell_locator]#convert the single tuple to a list of a single tuple
                cells = self.get_child_elements(row, cell_locator_lt)
                row_data.extend(cell.text.strip() for cell in cells)
            table_data.append(row_data)

        return table_data


    def switch_context_to_iframe(self,iframe_locator):
        """Switch to an iframe given the iframe locator"""
        try:
            iframe_element = self.get_element(iframe_locator)
            self.driver.switch_to.frame(iframe_element)
            print("Switched to iframe")
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error switching to iframe: {e}")

    def check_checkbox(self,checkbox_locator,onoff):
        """Toggle checkbox On or Off given the checkbox locator"""
        checkbox = self.get_element(checkbox_locator)
        if onoff=="ON":
            if not checkbox.is_selected():
                checkbox.click()

        elif onoff=="OFF":
            if checkbox.is_selected():
                checkbox.click()

    def set_slider_value(self, slider_locator, value):
        """Locate slider and set the slider value given an input value"""
        slider = self.get_element(slider_locator)

        # Execute JavaScript to get the min and max values, defaulting to 0 and 100 if not set
        min_value = self.driver.execute_script("return arguments[0].min || '0';", slider)
        max_value = self.driver.execute_script("return arguments[0].max || '100';", slider)

        # Convert min and max to integers
        min_value = int(min_value)
        max_value = int(max_value)

        # Ensure the value is within the min and max range
        if value < min_value or value > max_value:
            raise ValueError(f"Value {value} is out of range. Must be between {min_value} and {max_value}.")

        # Calculate the value to set
        value_to_set = min_value + ((max_value - min_value) * value / 100)

        # Set the value using JavaScript
        self.driver.execute_script("arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('change'));", slider, value_to_set)


    def get_progress_bar_value(self, progress_bar_locator):
        """Return value of a progress bar """
        # Locate the progress bar element
        progress_bar = self.get_element(progress_bar_locator)

        return progress_bar


    def get_shadow_root(self, host_locator):
        """Return shadow root """
        element = self._get_by_method(host_locator)
        return self.driver.execute_script('return arguments[0].shadowRoot', element)
        #this will return the shadow root and you can perform operations on that

    def click_shadow_child_element(self,host_locator, locators):
        """Click on shadow child element"""
        shadow_root = self.get_shadow_root(host_locator)
        wait = WebDriverWait(self.driver,10)
        for locator_type, locator_value in locators:
            try:
                by_method = self._get_by_method(locator_type)
                element = wait.until(
                    EC.visibility_of_element_located((by_method, locator_value))
                )#There is not a good way to use get_element here so we manually
                element.click()
            except (NoSuchElementException, TimeoutException):
                print(f"Locator failed: {locator_type}={locator_value}")
                continue

        raise NoSuchElementException(f"Element not found using any of the provided locators: {locators}")

    def WebDriverWait(self, driver, param):
        pass

    def find_text_on_page(self, text):
        """Searches for a given text anywhere on the page."""
        wait = WebDriverWait(self.driver,10)
        xpath = f"//*[contains(text(), '{text}')]"
        try:
            return wait.until(EC.presence_of_element_located((By.XPATH, xpath))).text
        except:
            return None  # Return None if the text is not found

    def wait_for_attribute_value_to_be(self, locators, attribute, expected_value, timeout=10):
        """
        Wait for an element's attribute to have a specific value.

        Args:
            locators (list): A list of locator tuples, e.g., [('XPATH', "//h3[...]")].
            attribute (str): The name of the attribute to check (e.g., 'aria-expanded').
            expected_value (str): The value the attribute is expected to have (e.g., 'true').
            timeout (int): The maximum time to wait for the condition.

        Returns:
            bool: True if the attribute is found with the expected value, False otherwise.
        """
        wait = WebDriverWait(self.driver, timeout)

        for locator_type, locator_value in locators:
            try:
                by_method = self._get_by_method(locator_type)

                # This is the key change! Use the correct expected condition.
                wait.until(
                    EC.text_to_be_present_in_element_attribute(
                        (by_method, locator_value),
                        attribute,
                        expected_value
                    )
                )
                print(f"Attribute '{attribute}' has value '{expected_value}' for locator: {locator_type}={locator_value}")
                return True # Success

            except (NoSuchElementException, TimeoutException):
                print(f"Locator failed or condition not met: {locator_type}={locator_value}")
                continue # Try the next locator in the list

        # If the loop finishes without returning True, no locator worked.
        print(f"All locators failed to find element with attribute '{attribute}' having value '{expected_value}'.")
        return False # Failure

    def is_text_present(self, text):
        """Checks if a given text exists anywhere on the page."""
        return self.find_text_on_page(text) is not None

    def take_screenshot(self, filename):
                 # --- Take a full page screenshot ---
        screenshot_filename = filename
        self.driver.save_screenshot('screenshots/'+screenshot_filename)
        print(f"Full page screenshot saved as {screenshot_filename}")
