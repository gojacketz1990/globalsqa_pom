import pytest
from pages.globalsqa_mainpage import GlobalsqaMainPage
import time

@pytest.mark.usefixtures("setup_globalsqa")
class TestWebTable:

    def test_webtable(self):

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

