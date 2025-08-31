import pytest
from pages.globalsqa_mainpage import GlobalsqaMainPage
import time
from utilities.LoggerBase import LoggerBase

@pytest.mark.usefixtures("setup_globalsqa")
class TestMultiForm(LoggerBase):

    def test_multiform(self, logger):
        logger.info("Starting test_multiform test")

        globalsqaPage = GlobalsqaMainPage(self.driver)
        angularjsPage = globalsqaPage.header.gotoAngularSitePage()

        uploadimagePage = angularjsPage.gotoUploadImage()
        time.sleep(2)
        uploadimagePage.upload_file_path("/Users/gojacketz/Desktop/GlobalsQA/Selenium/GlobalsQAPOM/data/Bo.jpg")


        max_retries = 10
        is_complete = False

        for _ in range(max_retries):
            # Wait a moment for the page to update
            time.sleep(1)

            # Get the new progress value as a string
            progress_value = uploadimagePage.get_upload_progress_value()

            if progress_value == "1":
                print("Upload completed successfully.")
                is_complete = True
                break

            print(f"Current progress value: '{progress_value}'")

        assert is_complete, f"Upload did not complete. Final value was: '{uploadimagePage.get_upload_progress_value()}'."
