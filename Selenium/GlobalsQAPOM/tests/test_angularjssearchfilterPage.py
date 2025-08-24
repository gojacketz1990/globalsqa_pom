import pytest
from pages.globalsqa_mainpage import GlobalsqaMainPage
import time
from utilities.LoggerBase import LoggerBase

@pytest.mark.usefixtures("setup_globalsqa")
class TestSearchFilter(LoggerBase):

    def test_searchfilter_payee(self, logger):

        from utilities.FakerHelper import FakerHelper
        data_generator = FakerHelper(locale='en_US')

        globalsqaPage = GlobalsqaMainPage(self.driver)
        angularjsPage = globalsqaPage.header.gotoAngularSitePage()

        searchfilterPage = angularjsPage.gotoSearchFilter()

        searchfilterPage.payee_search("Salary")

        # Get the row count
        row_count = searchfilterPage.get_number_of_rows()
        assert row_count == 1, f"Expected 1 rows, but found {row_count}"

        # Get all the data
        table_data = searchfilterPage.get_all_results_data()

        # Define the expected data
        expected_data = [
            ['1', 'Bank Savings', 'INCOME', 'Salary', '5000']
        ]

        # Verify the actual data matches the expected data
        assert table_data == expected_data, "Table data does not match expected data."

    def test_searchfilter_account(self):

        from utilities.FakerHelper import FakerHelper
        data_generator = FakerHelper(locale='en_US')

        globalsqaPage = GlobalsqaMainPage(self.driver)
        angularjsPage = globalsqaPage.header.gotoAngularSitePage()

        searchfilterPage = angularjsPage.gotoSearchFilter()

        searchfilterPage.account_search("Cash")

        # Get the row count
        row_count = searchfilterPage.get_number_of_rows()
        assert row_count == 3, f"Expected 3 rows, but found {row_count}"

        # Get all the data
        table_data = searchfilterPage.get_all_results_data()

        # Define the expected data
        expected_data = [
            ['1', 'Cash', 'EXPENDITURE', 'HouseRent', '1000'],
            ['2', 'Cash', 'EXPENDITURE', 'InternetBill', '1200'],
            ['3', 'Cash', 'EXPENDITURE', 'PowerBill', '200']
        ]

        # Verify the actual data matches the expected data
        assert table_data == expected_data, "Table data does not match expected data."

    def test_searchfilter_type(self):

        from utilities.FakerHelper import FakerHelper
        data_generator = FakerHelper(locale='en_US')

        globalsqaPage = GlobalsqaMainPage(self.driver)
        angularjsPage = globalsqaPage.header.gotoAngularSitePage()

        searchfilterPage = angularjsPage.gotoSearchFilter()

        searchfilterPage.search_by_type("INCOME")

        # Get the row count
        row_count = searchfilterPage.get_number_of_rows()
        assert row_count == 1, f"Expected 1 rows, but found {row_count}"

        # Get all the data
        table_data = searchfilterPage.get_all_results_data()

        # Define the expected data
        expected_data = [
            ['1', 'Bank Savings', 'INCOME', 'Salary', '5000']
        ]

        # Verify the actual data matches the expected data
        assert table_data == expected_data, "Table data does not match expected data."

    def test_searchfilter_expenditure_payee(self):

        from utilities.FakerHelper import FakerHelper
        data_generator = FakerHelper(locale='en_US')

        globalsqaPage = GlobalsqaMainPage(self.driver)
        angularjsPage = globalsqaPage.header.gotoAngularSitePage()

        searchfilterPage = angularjsPage.gotoSearchFilter()

        searchfilterPage.search_by_expenditure_payee("PowerBill")

        # Get the row count
        row_count = searchfilterPage.get_number_of_rows()
        assert row_count == 1, f"Expected 1 rows, but found {row_count}"

        # Get all the data
        table_data = searchfilterPage.get_all_results_data()

        # Define the expected data
        expected_data = [
            ['1', 'Cash', 'EXPENDITURE', 'PowerBill', '200']
        ]

        # Verify the actual data matches the expected data
        assert table_data == expected_data, "Table data does not match expected data."
