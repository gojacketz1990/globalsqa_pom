import pytest
from pages.globalsqa_mainpage import GlobalsqaMainPage
import time
from utilities.FakerHelper import FakerHelper
from utilities.LoggerBase import LoggerBase

@pytest.mark.usefixtures("setup_globalsqa")
class TestSamplePage(LoggerBase):


    def test_submission_with_empty_fields_shows_errors(self, logger):
        logger.info("Starting test_submission_with_empty_fields_shows_errors test")
        #This test does not work, the errors do not show up

        data_generator = FakerHelper(locale='en_US')

        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoSamplePage = demoPage.gotoSamplePage()

        #demoSamplePage.select_expertise_by_label("Automation Testing")

        #time.sleep(1)

        #demoSamplePage.select_education_option("Post Graduate")

        #time.sleep(3)

        #demoSamplePage.upload_file_path("/Users/gojacketz/Desktop/GlobalsQA/Selenium/GlobalsQAPOM/data/Bo.jpg")

        #time.sleep(3)

        #demoSamplePage.enter_name(data_generator.generate_full_name())

        #demoSamplePage.enter_email(data_generator.generate_email())

        #demoSamplePage.enter_website(data_generator.generate_website())

        demoSamplePage.select_experience("5-7")

        time.sleep(2)

        #demoSamplePage.click_alert_box()
        #time.sleep(2)

        #demoSamplePage.dismiss_chain_alerts()

        #time.sleep(1)

        #demoSamplePage.enter_comments("This is my comment")

        demoSamplePage.click_submit()

        assert demoSamplePage.is_error_block_displayed()

        # Verification Step 2: Retrieve the list of errors
        actual_errors = demoSamplePage.get_all_form_errors()
        expected_errors = [
            #"Name is required",
            "Email requires a valid email address"
            "Comment is required"
        ]

        # Assert that all expected errors are present
        assert set(expected_errors).issubset(set(actual_errors))

    def test_form_no_file(self):
        data_generator = FakerHelper(locale='en_US')

        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoSamplePage = demoPage.gotoSamplePage()

        demoSamplePage.select_expertise_by_label("Automation Testing")

        time.sleep(1)

        demoSamplePage.select_education_option("Post Graduate")

        time.sleep(3)

        demoSamplePage.upload_file_path("/Users/gojacketz/Desktop/GlobalsQA/Selenium/GlobalsQAPOM/data/Bo.jpg")

        #time.sleep(3)

        demoSamplePage.enter_name(data_generator.generate_full_name())

        demoSamplePage.enter_email(data_generator.generate_email())

        demoSamplePage.enter_website(data_generator.generate_website())

        demoSamplePage.select_experience("5-7")

        #demoSamplePage.click_alert_box()
        #time.sleep(2)

        #demoSamplePage.dismiss_chain_alerts()

        time.sleep(3)

        demoSamplePage.enter_comments("This is my comment")

        demoSamplePage.click_submit()

        time.sleep(3)

        #Verify message here

        # Call the page method to get the success message
        actual_message = demoSamplePage.get_success_message_text()

        # Assert that the message is correct
        expected_message = "Your message has been sent"
        assert actual_message == expected_message, \
            f"Expected success message '{expected_message}' but got '{actual_message}'"
