import pytest
from pages.globalsqa_mainpage import GlobalsqaMainPage
import time
from utilities.FakerHelper import FakerHelper
import random
import math

@pytest.mark.usefixtures("setup_globalsqa")
class TestConsumptionCalculator:

    def test_consumption(self):

        from utilities.FakerHelper import FakerHelper
        data_generator = FakerHelper(locale='en_US')

        globalsqaPage = GlobalsqaMainPage(self.driver)
        angularjsPage = globalsqaPage.header.gotoAngularSitePage()

        consumptioncalculatorPage = angularjsPage.gotoConsumptionCalculator()

        cups_of_coffee = random.randint(1,5)
        number_of_cigarettes = random.randint(1,5)

        # ... (Your test setup: navigate to the calculator page) ...

        # Enter a quantity for coffee
        consumptioncalculatorPage.enter_cups_of_coffee(cups_of_coffee)

        # Get the total caffeine from the page
        total_caffeine = consumptioncalculatorPage.get_total_caffeine()


        # Verify the total caffeine calculation (assuming 107.5mg per cup)
        expected_caffeine = cups_of_coffee * 107.5
        print(expected_caffeine)

        assert total_caffeine == math.floor(expected_caffeine + 0.5), f"Caffeine total is incorrect. Expected {math.floor(expected_caffeine + 0.5)}, got {total_caffeine}"


        if expected_caffeine > 400:
            # Assert that the warning is displayed
            assert consumptioncalculatorPage.is_caffeine_limit_exceeded(), "Caffeine limit warning was NOT displayed when it should have been."
        else:
            # Assert that the warning is NOT displayed
            assert not consumptioncalculatorPage.is_caffeine_limit_exceeded(), "Caffeine warning was displayed when it should NOT have been."

        # Enter a quantity for cigarettes
        consumptioncalculatorPage.enter_cigarettes(number_of_cigarettes)


        # Get the total tar from the page
        total_tar = consumptioncalculatorPage.get_total_tar()

        # Verify the total tar calculation (assuming 10mg per cigarette)
        expected_tar = number_of_cigarettes * 10
        assert total_tar == math.floor(expected_tar + 0.5), f"Tar total is incorrect. Expected {math.floor(expected_tar + 0.5)}, got {total_tar}"

        # Check if the total tar is over the limit and assert the warning appears
        if expected_tar >= 30:
            assert consumptioncalculatorPage.is_tar_limit_exceeded(), "Tar limit warning was NOT displayed when it should have been."
        else:
            assert not consumptioncalculatorPage.is_tar_limit_exceeded(), "Tar warning was displayed when it should NOT have been."
