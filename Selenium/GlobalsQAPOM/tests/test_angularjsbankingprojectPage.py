import pytest
from pages.globalsqa_mainpage import GlobalsqaMainPage
import time
from utilities.LoggerBase import LoggerBase
from utilities.FakerHelper import FakerHelper

@pytest.mark.usefixtures("setup_globalsqa")
class TestBankingProjectLogin(LoggerBase):

    def test_registration(self, logger):

        logger.info("Starting test_registration test")
        globalsqaPage = GlobalsqaMainPage(self.driver)
        angularjsPage = globalsqaPage.header.gotoAngularSitePage()

        bankingprojectPage = angularjsPage.gotoBankingProject()

        bankingprojectPage.click_customer_login_button()

        bankingprojectPage.select_name_dropdown("Albus Dumbledore")

        bankingprojectPage.click_login_button()

        time.sleep(2)
        welcome_name = bankingprojectPage.get_welcome_name()
        assert welcome_name == "Albus Dumbledore", f"Expected name 'Albus Dumbledore', but got '{welcome_name}'."

        # Get the account details from the page
        account_details = bankingprojectPage.get_account_details()

        # Assert that the retrieved values match the expected values
        assert account_details["account_number"] == "1010", "Account number is incorrect."
        assert account_details["balance"] == "0", "Balance is incorrect."
        assert account_details["currency"] == "Dollar", "Currency is incorrect."


    def test_deposit(self, logger):

        globalsqaPage = GlobalsqaMainPage(self.driver)
        angularjsPage = globalsqaPage.header.gotoAngularSitePage()

        bankingprojectPage = angularjsPage.gotoBankingProject()

        bankingprojectPage.click_customer_login_button()

        bankingprojectPage.select_name_dropdown("Albus Dumbledore")

        bankingprojectPage.click_login_button()

        time.sleep(2)
        welcome_name = bankingprojectPage.get_welcome_name()
        assert welcome_name == "Albus Dumbledore", f"Expected name 'Albus Dumbledore', but got '{welcome_name}'."

        # Get the account details from the page
        account_details = bankingprojectPage.get_account_details()

        # Assert that the retrieved values match the expected values
        #assert account_details["account_number"] == "1010", "Account number is incorrect."
        #assert account_details["balance"] == "0", "Balance is incorrect."
        #assert account_details["currency"] == "Dollar", "Currency is incorrect."

        current_balance = int(account_details["balance"])

        deposit_amount = 500
        bankingprojectPage.make_deposit(deposit_amount)

        # It's good practice to verify a success message
        # Add a method to your page object for this if needed
        # assert bankingprojectPage.is_transaction_successful(), "Deposit was not successful."

        # Step 3: Get the new balance and verifyac
        # Re-fetch the account details after the deposit
        new_account_details = bankingprojectPage.get_account_details()
        new_balance_str = new_account_details["balance"]

        # Convert the new balance to an integer
        new_balance = int(new_balance_str)

        # The final assertion
        expected_balance = current_balance + deposit_amount
        assert new_balance == expected_balance, f"Balance is incorrect. Expected {expected_balance}, but got {new_balance}."


    def test_failed_withdrawal(self, logger):

        globalsqaPage = GlobalsqaMainPage(self.driver)
        angularjsPage = globalsqaPage.header.gotoAngularSitePage()

        bankingprojectPage = angularjsPage.gotoBankingProject()

        bankingprojectPage.click_customer_login_button()

        bankingprojectPage.select_name_dropdown("Albus Dumbledore")

        bankingprojectPage.click_login_button()

        time.sleep(2)
        welcome_name = bankingprojectPage.get_welcome_name()
        assert welcome_name == "Albus Dumbledore", f"Expected name 'Albus Dumbledore', but got '{welcome_name}'."

        # Get the account details from the page
        account_details = bankingprojectPage.get_account_details()

        # Assert that the retrieved values match the expected values
        #assert account_details["account_number"] == "1010", "Account number is incorrect."
        #assert account_details["balance"] == "0", "Balance is incorrect."
        #assert account_details["currency"] == "Dollar", "Currency is incorrect."

        current_balance = int(account_details["balance"])

        # Attempt to withdraw more than the balance
        withdrawal_amount = current_balance + 1
        bankingprojectPage.make_withdrawal(withdrawal_amount)

        # Verify the error message
        is_error = bankingprojectPage.is_withdrawal_error_message_displayed()
        assert is_error, "Insufficient funds error message was not displayed."
        time.sleep(3)

        # Get the new balance and assert it has not changed
        new_balance = int(bankingprojectPage.get_account_details()["balance"])
        assert new_balance == current_balance, "Balance was changed, but should have remained the same."
        time.sleep(3)


    def test_successful_withdrawal(self, logger):

        globalsqaPage = GlobalsqaMainPage(self.driver)
        angularjsPage = globalsqaPage.header.gotoAngularSitePage()

        bankingprojectPage = angularjsPage.gotoBankingProject()

        bankingprojectPage.click_customer_login_button()

        bankingprojectPage.select_name_dropdown("Hermoine Granger")

        bankingprojectPage.click_login_button()

        time.sleep(2)
        welcome_name = bankingprojectPage.get_welcome_name()
        assert welcome_name == "Hermoine Granger", f"Expected name 'Hermoine Granger', but got '{welcome_name}'."

        # Get the account details from the page
        account_details = bankingprojectPage.get_account_details()

        # Assert that the retrieved values match the expected values
        #assert account_details["account_number"] == "1010", "Account number is incorrect."
        #assert account_details["balance"] == "0", "Balance is incorrect."
        #assert account_details["currency"] == "Dollar", "Currency is incorrect."

        current_balance = int(account_details["balance"])


        # Define the withdrawal amount
        withdrawal_amount = 50

        # Perform the withdrawal
        bankingprojectPage.make_withdrawal(withdrawal_amount)

        # Get the final account details
        final_account_details = bankingprojectPage.get_account_details()
        final_balance = int(final_account_details["balance"])

        # Verify the successful transaction message
        is_successful_message_displayed = bankingprojectPage.is_withdrawal_successful()
        assert is_successful_message_displayed, "Successful transaction message was not displayed."

        # Calculate the expected balance
        expected_balance = current_balance - withdrawal_amount

        # Assert that the final balance matches the expected balance
        assert final_balance == expected_balance, f"Balance is incorrect. Expected {expected_balance}, but got {final_balance}."


    def test_add_customer(self, logger):

        from utilities.FakerHelper import FakerHelper
        data_generator = FakerHelper(locale='en_US')

        globalsqaPage = GlobalsqaMainPage(self.driver)
        angularjsPage = globalsqaPage.header.gotoAngularSitePage()

        bankingprojectPage = angularjsPage.gotoBankingProject()

        bankingprojectPage.click_manager_login_button()

        bankingprojectPage.click_add_customer_button()

        firstname = data_generator.generate_first_name()
        lastname = data_generator.generate_last_name()
        postCode = data_generator.generate_zipcode()

        bankingprojectPage.add_customer(firstname,lastname,postCode)

        bankingprojectPage.click_customers_button()


        # Verify the customer is present in the table
        customer_is_present = bankingprojectPage.is_customer_present_in_table(
            firstname,
            lastname
        )

        # Assert that the customer was found in the table
        assert customer_is_present, f"Customer '{firstname} {lastname}' was not found in the customer table."



    def test_verify_customer_and_get_accounts(self, logger):

        from utilities.FakerHelper import FakerHelper
        data_generator = FakerHelper(locale='en_US')

        globalsqaPage = GlobalsqaMainPage(self.driver)
        angularjsPage = globalsqaPage.header.gotoAngularSitePage()

        bankingprojectPage = angularjsPage.gotoBankingProject()

        bankingprojectPage.click_manager_login_button()

        bankingprojectPage.click_customers_button()
        # Define the customer's name
        customer_first_name = "Hermoine"
        customer_last_name = "Granger"

        # Get and save the list of account numbers
        account_numbers = bankingprojectPage.get_customer_account_numbers(
            customer_first_name,
            customer_last_name
        )

        # Assert that the list of account numbers is not empty
        assert account_numbers, f"No account numbers found for {customer_first_name} {customer_last_name}."

        # Assert that the specific account numbers are in the list
        assert "1001" in account_numbers, "Account number 1001 not found."
        assert "1002" in account_numbers, "Account number 1002 not found."
        assert "1003" in account_numbers, "Account number 1003 not found."

        print(f"Verified that Hermoine Granger has accounts: {account_numbers}")


    def test_add_customer_and_account(self, logger):

        from utilities.FakerHelper import FakerHelper
        data_generator = FakerHelper(locale='en_US')

        globalsqaPage = GlobalsqaMainPage(self.driver)
        angularjsPage = globalsqaPage.header.gotoAngularSitePage()

        bankingprojectPage = angularjsPage.gotoBankingProject()

        bankingprojectPage.click_manager_login_button()

        bankingprojectPage.click_add_customer_button()

        firstname = data_generator.generate_first_name()
        lastname = data_generator.generate_last_name()
        full_name = f"{firstname} {lastname}"
        postCode = data_generator.generate_zipcode()

        bankingprojectPage.add_customer(firstname,lastname,postCode)

        bankingprojectPage.click_open_account_button()


        #bankingprojectPage.select_customer_by_name(full_name)

        #bankingprojectPage.select_currency("Dollar")

        bankingprojectPage.open_account(full_name,"Dollar")


        bankingprojectPage.click_customers_button()

        # Verify the customer is present in the table
        customer_is_present = bankingprojectPage.is_customer_present_in_table(
            firstname,
            lastname
        )

        # Assert that the customer was found in the table
        assert customer_is_present, f"Customer '{firstname} {lastname}' was not found in the customer table."

        account_numbers = bankingprojectPage.get_customer_account_numbers(
            firstname,
            lastname
        )

                # Assert that the list of account numbers is not empty
        assert account_numbers, f"No account numbers found for {firstname} {lastname}."

        print(account_numbers)

        time.sleep(5)






    def test_add_customer_and_delete_user(self, logger):

        from utilities.FakerHelper import FakerHelper
        data_generator = FakerHelper(locale='en_US')

        globalsqaPage = GlobalsqaMainPage(self.driver)
        angularjsPage = globalsqaPage.header.gotoAngularSitePage()

        bankingprojectPage = angularjsPage.gotoBankingProject()

        bankingprojectPage.click_manager_login_button()

        bankingprojectPage.click_add_customer_button()

        firstname = data_generator.generate_first_name()
        lastname = data_generator.generate_last_name()
        full_name = f"{firstname} {lastname}"
        postCode = data_generator.generate_zipcode()

        bankingprojectPage.add_customer(firstname,lastname,postCode)

        bankingprojectPage.click_open_account_button()


        #bankingprojectPage.select_customer_by_name(full_name)

        #bankingprojectPage.select_currency("Dollar")

        bankingprojectPage.open_account(full_name,"Dollar")


        bankingprojectPage.click_customers_button()

        # Verify the customer is present in the table
        customer_is_present = bankingprojectPage.is_customer_present_in_table(
            firstname,
            lastname
        )

        # Assert that the customer was found in the table
        assert customer_is_present, f"Customer '{firstname} {lastname}' was not found in the customer table."

        account_numbers = bankingprojectPage.get_customer_account_numbers(
            firstname,
            lastname
        )

        # Assert that the list of account numbers is not empty
        assert account_numbers, f"No account numbers found for {firstname} {lastname}."

        print(account_numbers)


        # Assert that the customer is initially present
        is_present_before = bankingprojectPage.is_customer_present_in_table(
            firstname,
            lastname
        )
        assert is_present_before, f"Customer {firstname} {lastname} was not found before deletion attempt."

        time.sleep(3)
        # Delete the customer
        bankingprojectPage.delete_customer(firstname, lastname)

        # Verify the customer is no longer present
        is_present_after = bankingprojectPage.is_customer_present_in_table(
            firstname,
            lastname
        )
        assert not is_present_after, f"Customer {firstname} {lastname} was still found after deletion."
