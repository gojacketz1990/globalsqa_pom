import pytest
from pages.globalsqa_mainpage import GlobalsqaMainPage
import time

@pytest.mark.usefixtures("setup_globalsqa")
class TestDraggableBox:

    def test_draggable_box(self):
        """
        Verifies that clicking the 'Start Download' button makes the
        file download dialog box appear.
        """        # Instantiate page objects
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoDraggableBoxPage = demoPage.gotoDraggableBox()
