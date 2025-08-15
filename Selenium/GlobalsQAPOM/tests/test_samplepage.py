import pytest
from pages.globalsqa_mainpage import GlobalsqaMainPage
import time
from utilities.FakerHelper import FakerHelper

@pytest.mark.usefixtures("setup_globalsqa")
class TestSamplePage:


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


    #
    # def test_alert_box(self):
    #
    #     data_generator = FakerHelper(locale='en_US')
    #
    #     globalsqaPage = GlobalsqaMainPage(self.driver)
    #     demoPage = globalsqaPage.header.gotoDemoSitePage()
    #
    #     # Step 1: Click the "Message Box" tab to reveal the download button
    #     demoSamplePage = demoPage.gotoSamplePage()
    #
    #     demoSamplePage.select_expertise_by_label("Automation Testing")
    #
    #     time.sleep(1)
    #
    #     demoSamplePage.select_education_option("Post Graduate")
    #
    #     time.sleep(3)
    #
    #     demoSamplePage.upload_file_path("/Users/gojacketz/Desktop/GlobalsQA/Selenium/GlobalsQAPOM/data/baseball.png")
    #
    #     time.sleep(3)
    #
    #     demoSamplePage.enter_name(data_generator.generate_full_name())
    #
    #     demoSamplePage.enter_email(data_generator.generate_email())
    #
    #     demoSamplePage.enter_website(data_generator.generate_website())
    #
    #     demoSamplePage.click_alert_box()
    #     time.sleep(2)
    #
    #     demoSamplePage.dismiss_chain_alerts()
    #
    #     time.sleep(3)
    #
    #     demoSamplePage.enter_comments("This is my comment")
    #
    #     demoSamplePage.click_submit()
    #
    #     time.sleep(3)

    def test_missing_fields(self):
        pass
