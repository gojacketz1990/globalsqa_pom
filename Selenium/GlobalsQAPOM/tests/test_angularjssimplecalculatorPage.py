import pytest
from pages.globalsqa_mainpage import GlobalsqaMainPage
import time
import random
from utilities.LoggerBase import LoggerBase

@pytest.mark.usefixtures("setup_globalsqa")
class TestSimpleCalculator(LoggerBase):

    def test_scrollable(self, logger):
        logger.info("Starting test_scrollable test")
        from utilities.FakerHelper import FakerHelper
        data_generator = FakerHelper(locale='en_US')

        globalsqaPage = GlobalsqaMainPage(self.driver)
        angularjsPage = globalsqaPage.header.gotoAngularSitePage()

        simplecalculatorPage = angularjsPage.gotoSimpleCalculator()

        a = random.randint(1,100)
        b = random.randint(1,100)
        operation = random.choice(["+","-","*","/"])
        #operation = random.choice(["/","/","/","/"])
        simplecalculatorPage.perform_calculation(a, b, operation)

        # Get the numbers and result from the page
        calculation_details = simplecalculatorPage.get_calculation_details()

        time.sleep(5)

        # Extract the numbers from the list and convert them to integers
        num1 = int(calculation_details[0])
        operator = calculation_details[1]
        num2 = int(calculation_details[2])
        actual_result = float(calculation_details[4])

            # Perform the calculation based on the operator string
        if operator == '+':
            expected_result = num1 + num2
        elif operator == '-':
            expected_result = num1 - num2
        elif operator == '*':
            expected_result = num1 * num2
        elif operator == '/':
            # Use integer division or float division depending on the calculator's behavior
            expected_result = num1 / num2
        else:
            # Handle unexpected operators
            raise ValueError(f"Unknown operator: {operator}")

        rounded_expected_result = round(expected_result, 10)
        rounded_actual_result = round(float(actual_result), 10)

        print(f"Verifying calculation. Expected: {rounded_expected_result}, Actual: {rounded_actual_result}")

        # Assert that the rounded results match
        assert rounded_actual_result == rounded_expected_result, f"Calculation failed. Expected {rounded_expected_result}, but got {rounded_actual_result}."

        print("Calculation verified successfully.")
