import pytest
from pages.globalsqa_mainpage import GlobalsqaMainPage
import time

@pytest.mark.usefixtures("setup_globalsqa")
class TestSamplePage:


    def test_expertise(self):
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoSamplePage = demoPage.gotoSamplePage()

        demoSamplePage.select_expertise_by_label("Automation Testing")

        time.sleep(1)

        demoSamplePage.select_education_option("Post Graduate")

        time.sleep(3)
