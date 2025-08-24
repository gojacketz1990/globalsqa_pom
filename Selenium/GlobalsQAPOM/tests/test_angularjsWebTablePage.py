import pytest
from pages.globalsqa_mainpage import GlobalsqaMainPage
import time
from utilities.LoggerBase import LoggerBase

@pytest.mark.usefixtures("setup_globalsqa")
class TestWebTable(LoggerBase):

    def test_webtable(self, logger):

        from utilities.FakerHelper import FakerHelper
        data_generator = FakerHelper(locale='en_US')

        globalsqaPage = GlobalsqaMainPage(self.driver)
        angularjsPage = globalsqaPage.header.gotoAngularSitePage()

        webtablePage = angularjsPage.gotoWebTable()

        webtablePage.first_name_search("Jac")

        time.sleep(3)

        webtablePage.first_name_search("")

        webtablePage.global_search("Jac")

        time.sleep(3)

    def test_webtable_data(self):

        from utilities.FakerHelper import FakerHelper
        data_generator = FakerHelper(locale='en_US')

        globalsqaPage = GlobalsqaMainPage(self.driver)
        angularjsPage = globalsqaPage.header.gotoAngularSitePage()

        webtablePage = angularjsPage.gotoWebTable()

        first_name = "Jacques"
        last_name = "Dupont"

        webtablePage.first_name_search(first_name)

        time.sleep(3)

        #webtablePage.first_name_search("")

        #webtablePage.global_search("Jac")

        #time.sleep(3)

        # The name you want to search for


        # Call the page method and assert that it returns True
        assert webtablePage.is_user_present_in_table(first_name), \
            f"Expected to find user '{first_name}' in the table, but they were not found."

        assert webtablePage.is_user_full_name_present_in_table(first_name, last_name), \
                f"Expected to find user '{first_name} {last_name}', but they were not found."

    def test_webtable_sort(self):

        from utilities.FakerHelper import FakerHelper
        data_generator = FakerHelper(locale='en_US')

        globalsqaPage = GlobalsqaMainPage(self.driver)
        angularjsPage = globalsqaPage.header.gotoAngularSitePage()

        webtablePage = angularjsPage.gotoWebTable()

        webtablePage.click_header_to_sort("lastName")

        is_sorted_ascending = webtablePage.is_column_sorted_correctly("lastName", "ascending")
        assert is_sorted_ascending, "Last Name column is not sorted in ascending order."


        # Click again to test descending sort
        webtablePage.click_header_to_sort("lastName")
        is_sorted_descending = webtablePage.is_column_sorted_correctly("lastName", "descending")
        assert is_sorted_descending, "Last Name column is not sorted in descending order."

    def test_webtable_numerical_sort(self):

        from utilities.FakerHelper import FakerHelper
        data_generator = FakerHelper(locale='en_US')

        globalsqaPage = GlobalsqaMainPage(self.driver)
        angularjsPage = globalsqaPage.header.gotoAngularSitePage()

        webtablePage = angularjsPage.gotoWebTable()

        webtablePage.click_header_to_sort("balance")
        is_sorted_ascending = webtablePage.is_column_sorted_correctly("balance", "ascending")
        assert is_sorted_ascending, "Balance column is not sorted in ascending order."

        # Click again to test descending sort
        webtablePage.click_header_to_sort("balance")
        is_sorted_ascending = webtablePage.is_column_sorted_correctly("balance", "descending")
        assert is_sorted_ascending, "Balance column is not sorted in descending order."

        # Click again to test descending sort
        webtablePage.click_header_to_sort("age")
        is_sorted_ascending = webtablePage.is_column_sorted_correctly("age", "ascending")
        assert is_sorted_ascending, "Age column is not sorted in ascending order."

        # Click again to test descending sort
        webtablePage.click_header_to_sort("age")
        is_sorted_ascending = webtablePage.is_column_sorted_correctly("age", "descending")
        assert is_sorted_ascending, "Age column is not sorted in descending order."
