from pages.BasePage import BasePage
from pages.Header_Components import HeaderComponent
from locators.angularjs_bankingproject_locators import AngularJSBankingProjectPageLocators
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
import time
import datetime
import pytest
import re
import json

class AngularJSBankingProjectPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.angularJSBankingProjectPageLocators = AngularJSBankingProjectPageLocators()

    def click_home_button(self):
        self.element_click(AngularJSBankingProjectPageLocators.home_button_locator)

    def click_customer_login_button(self):
        self.element_click(AngularJSBankingProjectPageLocators.customer_login_locator)

    def click_manager_login_button(self):
        self.element_click(AngularJSBankingProjectPageLocators.bank_manager_login_locator)

    def select_name_dropdown(self,name):
        self.select_from_dropdown_by_visible_text(AngularJSBankingProjectPageLocators.customer_name_dropdown_locator,name)

    def click_login_button(self):
        self.element_click(AngularJSBankingProjectPageLocators.login_button_locator)


    def get_welcome_name(self) -> str:
        """Retrieves the name from the welcome message."""
        return self.get_element_text(AngularJSBankingProjectPageLocators.welcome_name_locator)

    def get_account_details(self) -> dict:
        """
        Retrieves the account number, balance, and currency.

        Returns:
            dict: A dictionary containing the account details.
        """
        account_number = self.get_element_text(AngularJSBankingProjectPageLocators.account_number_locator)
        balance = self.get_element_text(AngularJSBankingProjectPageLocators.balance_locator)
        currency = self.get_element_text(AngularJSBankingProjectPageLocators.currency_locator)

        return {
            "account_number": account_number.strip(),
            "balance": balance.strip(),
            "currency": currency.strip()
        }



    def make_deposit(self, amount: int):
        """Performs a deposit of a specified amount."""
        self.logger.info(f"Attempting to deposit {amount}.")

        # Click the Deposit tab
        self.element_click(AngularJSBankingProjectPageLocators.deposit_button_locator)

        # Find the amount input field
        amount_input = self.get_element(AngularJSBankingProjectPageLocators.deposit_amount_locator)

        # Enter the amount and submit
        amount_input.send_keys(str(amount))
        self.element_click(AngularJSBankingProjectPageLocators.make_deposit_button_locator)

    def make_withdrawal(self, amount: str):
        """
        Performs a withdrawal of a specified amount.
        Returns the browser validation message if an invalid amount is entered.
        """
        self.logger.info(f"Attempting to withdraw {amount}.")

        # Click the Withdrawal tab
        self.element_click(AngularJSBankingProjectPageLocators.withdrawal_button_locator)
        time.sleep(2)

        # Find the amount input field
        amount_input = self.get_element(AngularJSBankingProjectPageLocators.withdrawal_amount_locator)

        # Enter the amount and click the submit button
        amount_input.send_keys(amount)
        self.element_click(AngularJSBankingProjectPageLocators.make_withdrawal_button_locator)

        # Check if a browser validation message is present
        validation_message = self.get_element_attribute(
            AngularJSBankingProjectPageLocators.withdrawal_amount_locator,
            "validationMessage"
        )

        # Return the message if it exists, otherwise return None
        return validation_message if validation_message else None

    def get_transaction_message_text(self) -> str:
        """
        Retrieves the text from the transaction message span using textContent.
        This works even if the element is not yet visible.
        """
        # The locator is a list of tuples, just like your other locators
        return self.get_element_text_content(
            AngularJSBankingProjectPageLocators.transaction_message_locator
        )

    def get_withdrawal_input_validation_message(self) -> str:
        """
        Retrieves the browser's validation message from the withdrawal input field.
        """
        # Assuming AngularJSBankingProjectPageLocators has a locator for the withdrawal input
        locator = AngularJSBankingProjectPageLocators.withdrawal_amount_locator

        # Use the generic method from BasePage to get the attribute
        print(self.get_element_attribute(locator, "validationMessage"))
        return self.get_element_attribute(locator, "validationMessage")

    # In your Page Object class
    def is_withdrawal_successful(self) -> bool:
        """Verifies that the successful withdrawal message is displayed."""
        return self.is_text_present_in_element(AngularJSBankingProjectPageLocators.withdraw_message_locator, "Transaction successful")

    def is_withdrawal_error_message_displayed(self) -> bool:
        """Checks if the withdrawal error message is displayed."""
        # Using 'contains' is safer as the full error message is long.
        return self.is_text_present_in_element(AngularJSBankingProjectPageLocators.withdraw_message_locator, "Transaction Failed. You can not withdraw amount more than the balance.")

    #Manager methods

    def click_add_customer_button(self):
        self.element_click(AngularJSBankingProjectPageLocators.add_customer_button_locator)

    def click_open_account_button(self):
        self.element_click(AngularJSBankingProjectPageLocators.open_account_button_locator)

    def select_customer_by_name(self, customer_name: str):
        """Selects a customer from the dropdown by their full name."""
        self.logger.info(f"Selecting customer '{customer_name}' from dropdown.")
        self.select_from_dropdown_by_visible_text(AngularJSBankingProjectPageLocators.open_account_customer_dropdown_locator, customer_name)


    def select_currency(self, currency):
        self.select_from_dropdown_by_visible_text(AngularJSBankingProjectPageLocators.currency_dropdown_locator, currency)

    def process_new_account(self):
        self.element_click(AngularJSBankingProjectPageLocators.process_new_account_button)


    def open_account(self,customer_name, currency):

        self.select_customer_by_name(customer_name)
        self.select_currency(currency)
        self.process_new_account()
        self.dismiss_all_alerts()


    def click_customers_button(self):
        self.element_click(AngularJSBankingProjectPageLocators.customers_button_locator)

    def add_customer(self, firstName, lastName, postCode):
        self.click_add_customer_button()
        self.type_into_element(firstName, AngularJSBankingProjectPageLocators.add_customer_first_name_locator)
        self.type_into_element(lastName, AngularJSBankingProjectPageLocators.add_customer_last_name_locator)
        self.type_into_element(postCode, AngularJSBankingProjectPageLocators.add_customer_post_code_locator)
        self.element_click(AngularJSBankingProjectPageLocators.add_customer_submit_locator)
        self.dismiss_all_alerts()

    def is_customer_present_in_table(self, first_name: str, last_name: str) -> bool:
        """
        Checks if a customer is present in the table based on their first and last name.
        """
        # Use the dynamic locator to create a specific XPath for the customer
        customer_locator = self.get_dynamic_locator_multiple(
            AngularJSBankingProjectPageLocators.customer_row,
            first_name,
            last_name
        )

        # Check if the element exists in the DOM
        is_present = self.is_element_present(customer_locator)

        self.logger.info(f"Checking for customer '{first_name} {last_name}'. Found: {is_present}")
        return is_present

    def is_customer_and_account_populated(self, first_name: str, last_name: str) -> bool:
        """
        Checks if a customer exists in the table and their account number is populated.
        """
        # Use the new dynamic locator
        customer_account_locator = self.get_dynamic_locator_multiple(
            AngularJSBankingProjectPageLocators.customer_and_account,
            first_name,
            last_name
        )

        # Check for the existence of the element
        is_present = self.is_element_present(customer_account_locator)

        self.logger.info(f"Checking for '{first_name} {last_name}' and populated account. Result: {is_present}")
        return is_present


    def get_customer_account_numbers(self, first_name: str, last_name: str) -> list:
        """
        Finds a customer's row and returns a list of their account numbers.
        """
        try:
            # Use a dynamic locator to find the customer's row (the parent element)
            customer_row_locator = self.get_dynamic_locator_multiple(
                AngularJSBankingProjectPageLocators.customer_row,
                first_name,
                last_name
            )
            customer_row_element = self.get_element(customer_row_locator)

            # Get the <td> element that contains the account numbers
            account_cell_locator = [("xpath", "./td[4]")]  # The 4th <td> contains accounts
            account_cell_element = self.get_child_element(customer_row_element, account_cell_locator)

            # Now, get all the account number spans within that cell
            account_number_spans = self.get_child_elements(account_cell_element, AngularJSBankingProjectPageLocators.account_number_spans)

            # Extract the text and remove any leading/trailing whitespace
            account_numbers = [span.text.strip() for span in account_number_spans]

            self.logger.info(f"Retrieved account numbers for {first_name} {last_name}: {account_numbers}")
            return account_numbers

        except NoSuchElementException:
            self.logger.error(f"Could not find customer '{first_name} {last_name}' to get account numbers.")
            return []


    def delete_customer(self, first_name: str, last_name: str):
        """
        Deletes a customer from the table by clicking their Delete button.
        """
        self.logger.info(f"Attempting to delete customer '{first_name} {last_name}'.")

        # Get the dynamic locator for the specific customer's delete button
        delete_button_locator = self.get_dynamic_locator_multiple(
            AngularJSBankingProjectPageLocators.delete_customer_button,
            first_name,
            last_name
        )

        # Click the button using your existing element_click method
        self.element_click(delete_button_locator)
