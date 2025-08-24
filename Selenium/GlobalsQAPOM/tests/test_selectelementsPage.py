import pytest
from pages.globalsqa_mainpage import GlobalsqaMainPage
import time
from utilities.LoggerBase import LoggerBase

@pytest.mark.usefixtures("setup_globalsqa")
class TestSelectElements(LoggerBase):

    def test_select_multiple_selection(self, logger):
        logger.info("Starting test_select_multiple_selection test")
        """
        Verifies that clicking the 'Start Download' button makes the
        file download dialog box appear.
        """

        # Instantiate page objects
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoSelectElementsPage = demoPage.gotoSelectElements()

        demoSelectElementsPage.select_multiple_items_by_text(["Item 5"])

        time.sleep(3)

    def test_select_multiple_items(self):
        """
        Verifies that clicking the 'Start Download' button makes the
        file download dialog box appear.
        """

        # Instantiate page objects
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoSelectElementsPage = demoPage.gotoSelectElements()

        items_to_select = ["Item 2", "Item 4", "Item 6"]

        demoSelectElementsPage.select_multiple_items_by_text(items_to_select)

        demoSelectElementsPage.verify_selected_items(items_to_select)

        time.sleep(3)




    def test_select_multiple_grid_selection(self):
        """
        Verifies that clicking the 'Start Download' button makes the
        file download dialog box appear.
        """

        # Instantiate page objects
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoSelectElementsPage = demoPage.gotoSelectElements()

        demoSelectElementsPage.click_grid_selection_tab()

        #demoSelectElementsPage.select_grid_item_by_text("5")
        items_to_select = ["4"]

        demoSelectElementsPage.select_multiple_grid_items_by_text(items_to_select)

        demoSelectElementsPage.verify_grid_selected_items(items_to_select)

        time.sleep(3)

    def test_select_multiple_grid_items(self):
        """
        Verifies that clicking the 'Start Download' button makes the
        file download dialog box appear.
        """

        # Instantiate page objects
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoSelectElementsPage = demoPage.gotoSelectElements()

        demoSelectElementsPage.click_grid_selection_tab()

        items_to_select = ["2", "12", "6"]

        demoSelectElementsPage.select_multiple_grid_items_by_text(items_to_select)

        demoSelectElementsPage.verify_grid_selected_items(items_to_select)

        time.sleep(3)




    def test_drag_and_drop_serialize_selection(self):
        """
        Tests the drag-and-drop multiselect functionality.
        """

        # Instantiate page objects
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoSelectElementsPage = demoPage.gotoSelectElements()

        selected_items = ["Item 1","Item 2", "Item 3", "Item 4", "Item 5", "Item 6"]
        start_item = "Item 1"
        end_item = "Item 6"
        # Call the method
        expected_select_text = "#1 #2 #3 #4 #5 #6"

        demoSelectElementsPage.click_serialize_tab()
        demoSelectElementsPage.select_serialize_items_with_drag_and_drop(start_text=start_item, end_text=end_item)

        demoSelectElementsPage.verify_serialize_selection_text(expected_select_text)

        demoSelectElementsPage.verify_selected_serialize_items(selected_items)


    def test_select_serialize_single_selection(self):
        """
        Verifies that clicking the 'Start Download' button makes the
        file download dialog box appear.
        """

        # Instantiate page objects
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoSelectElementsPage = demoPage.gotoSelectElements()

        demoSelectElementsPage.click_serialize_tab()

        demoSelectElementsPage.verify_serialize_selection_text("none")

        #demoSelectElementsPage.select_grid_item_by_text("5")
        items_to_select = ["Item 4"]
        expected_select_text = "#4"

        demoSelectElementsPage.select_multiple_serialize_items_by_text(items_to_select)

        demoSelectElementsPage.verify_serialize_selection_text(expected_select_text)

        demoSelectElementsPage.verify_selected_serialize_items(items_to_select)

        time.sleep(3)

    def test_select_multiple_serialize_items(self):
        """
        Verifies that clicking the 'Start Download' button makes the
        file download dialog box appear.
        """

        # Instantiate page objects
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoSelectElementsPage = demoPage.gotoSelectElements()

        demoSelectElementsPage.click_serialize_tab()

        items_to_select = ["Item 1", "Item 4", "Item 6"]

        expected_select_text = "#1 #4 #6"

        demoSelectElementsPage.select_multiple_serialize_items_by_text(items_to_select)

        demoSelectElementsPage.verify_serialize_selection_text(expected_select_text)

        demoSelectElementsPage.verify_selected_serialize_items(items_to_select)

        time.sleep(3)



