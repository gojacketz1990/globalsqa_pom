import pytest
from pages.globalsqa_mainpage import GlobalsqaMainPage
import time

@pytest.mark.usefixtures("setup_globalsqa")
class TestDraggableBox:

    def test_multiform(self):

        from utilities.FakerHelper import FakerHelper
        data_generator = FakerHelper(locale='en_US')

        globalsqaPage = GlobalsqaMainPage(self.driver)
        angularjsPage = globalsqaPage.header.gotoAngularSitePage()

        multiformPage = angularjsPage.gotoMultiForm()

        time.sleep(3)

        submitted_name = data_generator.generate_full_name()
        multiformPage.enter_name(submitted_name)

        submitted_email = data_generator.generate_email()

        multiformPage.enter_email(submitted_email)

        multiformPage.click_next_section_button()

        time.sleep(1)

        assert multiformPage.is_interests_page_displayed(), \
            "The 'Interests' page header was not displayed."

        time.sleep(3)

        submitted_data = multiformPage.get_json_submitted()

        # Assertions to verify the data
        expected_name = submitted_name
        expected_email = submitted_email

        assert submitted_data['name'] == expected_name, f"Expected name: {expected_name}, but got: {submitted_data['name']}"
        assert submitted_data['email'] == expected_email, f"Expected email: {expected_email}, but got: {submitted_data['email']}"

        # You can also assert that keys exist in the json
        assert 'name' in submitted_data
        assert 'email' in submitted_data



    def test_no_email(self):

        from utilities.FakerHelper import FakerHelper
        data_generator = FakerHelper(locale='en_US')

        globalsqaPage = GlobalsqaMainPage(self.driver)
        angularjsPage = globalsqaPage.header.gotoAngularSitePage()

        multiformPage = angularjsPage.gotoMultiForm()

        time.sleep(3)

        submitted_name = data_generator.generate_full_name()
        multiformPage.enter_name(submitted_name)

        submitted_email = data_generator.generate_email()

        multiformPage.enter_email(submitted_email)

        multiformPage.click_next_section_button()

        time.sleep(1)

        assert multiformPage.is_interests_page_displayed(), \
            "The 'Interests' page header was not displayed."

        time.sleep(3)

        submitted_data = multiformPage.get_json_submitted()

        # Assertions to verify the data
        expected_name = submitted_name
        expected_email = submitted_email

        assert submitted_data['name'] == expected_name, f"Expected name: {expected_name}, but got: {submitted_data['name']}"
        assert submitted_data['email'] == expected_email, f"Expected email: {expected_email}, but got: {submitted_data['email']}"

        # You can also assert that keys exist in the json
        assert 'name' in submitted_data
        assert 'email' in submitted_data

        multiformPage.select_radio_button_by_value("xbox")

        assert multiformPage.is_radio_button_selected("xbox")

        multiformPage.click_next_section_button()

        # Verification Step: Get the message and assert it is correct
        actual_message = multiformPage.get_payment_success_message()
        expected_message = "Thanks For Your Money!"

        assert actual_message == expected_message, \
            f"Expected success message '{expected_message}' but got '{actual_message}'"

        submitted_data = multiformPage.get_json_submitted()

        # Assertions to verify the data
        expected_name = submitted_name
        expected_email = submitted_email
        expected_console = "xbox"

        assert submitted_data['name'] == expected_name, f"Expected name: {expected_name}, but got: {submitted_data['name']}"
        assert submitted_data['email'] == expected_email, f"Expected email: {expected_email}, but got: {submitted_data['email']}"
        assert submitted_data['type'] == expected_console, f"Expected console: {expected_console}, but got: {submitted_data['type']}"

        # You can also assert that keys exist in the json
        assert 'name' in submitted_data
        assert 'email' in submitted_data
        assert 'type' in submitted_data
