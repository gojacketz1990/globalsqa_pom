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

        # You can also assert that keys exist
        assert 'name' in submitted_data
        assert 'email' in submitted_data
