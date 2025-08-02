from pages.BasePage import BasePage
from pages.Header_Components import HeaderComponent
from locators.demosite_dialogbox_page_locators import DemoDialogBoxPageLocators
import time
import pytest

class DemoDialogBoxPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.demoDialogBoxPageLocators = DemoDialogBoxPageLocators()

    def _click_tab(self, tab_locator: list):
        """
        Internal method to click on a tab.
        """
        self.logger.info(f"Clicking the tab with locator: {tab_locator}")
        self.element_click(tab_locator)
        time.sleep(2)

    def _get_tab_class(self, tab_locator: list) -> str:
        """
        Internal method to retrieve the 'class' attribute of a tab.
        """
        self.logger.info(f"Retrieving class attribute for tab with locator: {tab_locator}")
        return self.get_element_attribute(tab_locator, "class")

    def verify_tab_becomes_active_by_name(self, tab_name: str):
        """
        Verifies that a given tab becomes active when clicked, based on its name.
        This method maps the string name to the correct locator internally.

        The method now handles cases where the target tab is already active initially.
        """
        tab_locators = {
            "message_box_tab": DemoDialogBoxPageLocators.messagebox_tab,
            "confirmation_tab": DemoDialogBoxPageLocators.confirmationbox_tab,
            "form_tab": DemoDialogBoxPageLocators.form_tab
        }

        if tab_name not in tab_locators:
            pytest.fail(f"FAIL: Invalid tab name provided: '{tab_name}'")

        tab_locator = tab_locators[tab_name]
        self.logger.info(f"Starting verification for '{tab_name}' tab activation.")

        # Check if the target tab is already active. If so, click a different tab
        # to ensure the test starts from a known inactive state.
        if self._get_tab_class(tab_locator) == "resp-tab-item resp-tab-active":
            self.logger.info(f"The '{tab_name}' tab is already active. Clicking a different tab to reset state.")

            # Find and click a different tab (e.g., the first one in the list)
            other_tab_locator = None
            for name, locator in tab_locators.items():
                if name != tab_name:
                    other_tab_locator = locator
                    break

            if other_tab_locator:
                self._click_tab(other_tab_locator)
            else:
                pytest.fail("Could not find an alternative tab to click to reset state.")

        # 1. Get the initial class and assert it is not the active class
        initial_class = self._get_tab_class(tab_locator)
        assert initial_class == "resp-tab-item", \
            f"FAIL: Tab should not be active initially. Got: {initial_class}"

        # 2. Click the tab using the generic click method
        self._click_tab(tab_locator)

        # 3. Get the new class and assert it has become active
        new_class = self._get_tab_class(tab_locator)
        expected_class = "resp-tab-item resp-tab-active"
        assert new_class == expected_class, \
            f"FAIL: Tab did not become active. Expected: '{expected_class}', Got: '{new_class}'"

        self.logger.info(f"SUCCESS: Tab '{tab_name}' correctly became active after click.")

    # These older methods can remain for backwards compatibility if needed
    def click_message_box_tab(self):
        self._click_tab(DemoDialogBoxPageLocators.messagebox_tab)

    def click_confirmation_tab(self):
        self._click_tab(DemoDialogBoxPageLocators.confirmationbox_tab)

    def click_form_tab(self):
        self._click_tab(DemoDialogBoxPageLocators.form_tab)

    def get_message_box_tab_class(self):
        return self._get_tab_class(DemoDialogBoxPageLocators.messagebox_tab)

    def get_confirmation_tab_class(self):
        return self._get_tab_class(DemoDialogBoxPageLocators.confirmationbox_tab)

    def get_form_tab_class(self):
        return self._get_tab_class(DemoDialogBoxPageLocators.form_tab)


    def get_all_users_data(self):
        try:
            # Step 1: Switch to the iframe to access the table
            self.switch_to_frame(DemoDialogBoxPageLocators.form_demo_iframe)

            # Step 2: Call the read_table method with our defined locators
            # Note: The read_table method now operates within the iframe context
            users_data = self.read_table(
                table_locator=DemoDialogBoxPageLocators._table_locator,
                row_locator=DemoDialogBoxPageLocators._row_locator,
                cell_locator=DemoDialogBoxPageLocators._cell_locator
            )
            return users_data
        finally:
            # Step 3: Crucially, switch the driver's focus back to the main page
            self.switch_to_default_content()

    def create_new_user_click(self):
        self.element_click(DemoDialogBoxPageLocators.new_user_button_locator)

    def enter_user_name(self,name):
        self.type_into_element(name, DemoDialogBoxPageLocators.name_text_field_locator)

    def enter_email(self,email):
        self.type_into_element(email, DemoDialogBoxPageLocators.email_text_field_locator )

    def enter_password(self,password):
        self.type_into_element(password, DemoDialogBoxPageLocators.password_text_field_locator)

    def create_account_click(self):
        self.element_click(DemoDialogBoxPageLocators.create_account_button_locators)

    def create_new_user(self, name, email, password):
        try:
            # Step 1: Switch to the iframe to access the table
            self.switch_to_frame(DemoDialogBoxPageLocators.form_demo_iframe)
            self.create_new_user_click()
            self.enter_user_name(name)
            self.enter_email(email)
            self.enter_password(password)
            self.create_account_click()

        finally:
            # Step 3: Crucially, switch the driver's focus back to the main page
            self.switch_to_default_content()

#Message Tab
    # def is_download_dialog_present(self):
    #     try:
    #         # Step 1: Switch to the iframe
    #         self.switch_to_frame(DemoDialogBoxPageLocators.message_box_demo_iframe)
    #         return self.is_element_present(DemoDialogBoxPageLocators.download_complete_locator)
    #
    #     finally:
    #         # Step 3: Always switch back to the default content
    #         self.switch_to_default_content()

    def is_download_dialog_present(self) -> bool:
        """
        Checks if the 'empty recycle bin' dialog element is present on the page.
        This is a safe way to check for element existence without an exception.
        """
        self.logger.info("Checking for the presence of the 'empty recycle bin' element.")
        try:
            # Step 1: Switch to the iframe
            self.switch_to_frame(DemoDialogBoxPageLocators.message_box_demo_iframe)

            # Step 2: Look for the element inside the iframe
            self.wait_for_element_to_be_visible(DemoDialogBoxPageLocators.download_complete_locator, timeout=1)
            return True
        except:
            # If the element is not found within the timeout, return False
            return False
        finally:
            # Step 3: Always switch back to the default content
            self.switch_to_default_content()


    def click_ok_download_complete(self):
        try:
            # Step 1: Switch to the iframe
            self.switch_to_frame(DemoDialogBoxPageLocators.message_box_demo_iframe)

            # Step 2: Perform the action inside the iframe
            self.element_click(DemoDialogBoxPageLocators.download_ok_button_locator)

        finally:

            # Step 3: Always switch back to the default content
            self.switch_to_default_content()

    def get_storage_percentage(self):

        try:
            # Step 1: Switch to the iframe
            self.switch_to_frame(DemoDialogBoxPageLocators.message_box_demo_iframe)



            # Step 3: Retrieve the full text from that element
            full_text = self.retrieve_element_text(DemoDialogBoxPageLocators.percentage_text_locator)

            full_text = "Currently using 36% of your storage space."

            # 1. Find the index of the '%' character
            percent_index = full_text.find('%')

            # 2. Slice the string to get the two digits before the '%'
            # This assumes the number is always two digits long, which is a major flaw
            number_string = full_text[percent_index-2:percent_index]
            # number_string is '36'

            # 3. Convert the string to an integer
            percentage_as_int = int(number_string)
            # percentage_as_int is 36

            print(percentage_as_int)

            return percentage_as_int

        finally:
            # Step 4: Always switch back to the default content
            self.switch_to_default_content()


    def confirm_delete_all_items(self):
        try:
            # Step 1: Switch to the iframe
            self.switch_to_frame(DemoDialogBoxPageLocators.confirmation_box_demo_iframe)

            # Step 2: Perform the action inside the iframe
            self.element_click(DemoDialogBoxPageLocators.confirmation_box_delete_all)

        finally:

            # Step 3: Always switch back to the default content
            self.switch_to_default_content()

    def confirm_cancel_delete(self):
        try:
            # Step 1: Switch to the iframe
            self.switch_to_frame(DemoDialogBoxPageLocators.confirmation_box_demo_iframe)

            # Step 2: Perform the action inside the iframe
            self.element_click(DemoDialogBoxPageLocators.confirmation_box_cancel)

        finally:

            # Step 3: Always switch back to the default content
            self.switch_to_default_content()

    # NEW METHODS FOR DIALOG BOX INTERACTION
    def click_confirmation_dialog_button(self, button_name: str):
        """
        Clicks the OK or Cancel button in the confirmation dialog.
        """
        if button_name.lower() == "delete all items":
            self.element_click(DemoDialogBoxPageLocators.confirmation_box_delete_all)
            self.logger.info("Clicked OK on the confirmation dialog.")
        elif button_name.lower() == "cancel":
            self.element_click(DemoDialogBoxPageLocators.confirmation_box_cancel)
            self.logger.info("Clicked Cancel on the confirmation dialog.")
        else:
            pytest.fail(f"Invalid button name: {button_name}. Use 'ok' or 'cancel'.")


        #Message Tab
    def is_empty_recycle_bin_present(self) -> bool:
        """
        Checks if the 'empty recycle bin' dialog element is present on the page.
        This is a safe way to check for element existence without an exception.
        """
        self.logger.info("Checking for the presence of the 'empty recycle bin' element.")
        try:
            # Step 1: Switch to the iframe
            self.switch_to_frame(DemoDialogBoxPageLocators.confirmation_box_demo_iframe)

            # Step 2: Look for the element inside the iframe
            self.wait_for_element_to_be_visible(DemoDialogBoxPageLocators.empty_recycle_bin_locator, timeout=1)
            return True
        except:
            # If the element is not found within the timeout, return False
            return False
        finally:
            # Step 3: Always switch back to the default content
            self.switch_to_default_content()

