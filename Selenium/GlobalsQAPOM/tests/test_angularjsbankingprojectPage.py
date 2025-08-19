import pytest
from pages.globalsqa_mainpage import GlobalsqaMainPage
import time
from utilities.FakerHelper import FakerHelper

@pytest.mark.usefixtures("setup_globalsqa")
class TestBankingProjectLogin:

    def test_registration(self):

        from utilities.FakerHelper import FakerHelper
        data_generator = FakerHelper(locale='en_US')

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


    def test_deposit(self):

        from utilities.FakerHelper import FakerHelper
        data_generator = FakerHelper(locale='en_US')

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

        # Step 3: Get the new balance and verify
        # Re-fetch the account details after the deposit
        new_account_details = bankingprojectPage.get_account_details()
        new_balance_str = new_account_details["balance"]

        # Convert the new balance to an integer
        new_balance = int(new_balance_str)

        # The final assertion
        expected_balance = current_balance + deposit_amount
        assert new_balance == expected_balance, f"Balance is incorrect. Expected {expected_balance}, but got {new_balance}."


