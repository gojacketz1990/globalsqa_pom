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

    def make_withdrawal(self, amount: int):
        """Performs a deposit of a specified amount."""
        self.logger.info(f"Attempting to withdraw {amount}.")

        # Click the Deposit tab
        self.element_click(AngularJSBankingProjectPageLocators.withdrawal_button_locator)

        # Find the amount input field
        amount_input = self.get_element(AngularJSBankingProjectPageLocators.withdrawal_amount_locator)

        # Enter the amount and submit
        amount_input.send_keys(str(amount))
        self.element_click(AngularJSBankingProjectPageLocators.make_withdrawal_button_locator)

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
