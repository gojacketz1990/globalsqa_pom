import pytest
from pages.globalsqa_mainpage import GlobalsqaMainPage
import time

@pytest.mark.usefixtures("setup_globalsqa")
class TestSorting:

    def test_drag_and_drop_to_sort(self):
        """
        Verifies that clicking the 'Start Download' button makes the
        file download dialog box appear.
        """

        # Instantiate page objects
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoSortingPage = demoPage.gotoSorting()

        demoSortingPage.click_portlets_tab()

        start_item = "Images"
        end_item = "Feeds"
        # Call the method
        demoSortingPage.portlets_drag_and_drop_to_sort(start_text=start_item, end_text=end_item)
        time.sleep(1)

        start_item = "Links"
        end_item = "Images"
        # Call the method
        demoSortingPage.portlets_drag_and_drop_to_sort(start_text=start_item, end_text=end_item)
        time.sleep(1)

        start_item = "Shopping"
        end_item = "Links"
        # Call the method
        demoSortingPage.portlets_drag_and_drop_to_sort(start_text=start_item, end_text=end_item)
        time.sleep(1)

        start_item = "News"
        end_item = "Shopping"
        # Call the method
        demoSortingPage.portlets_drag_and_drop_to_sort(start_text=start_item, end_text=end_item)
        time.sleep(1)


    def test_multiple_lists(self):
        """
        Verifies that clicking the 'Start Download' button makes the
        file download dialog box appear.
        """

        # Instantiate page objects
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoSortingPage = demoPage.gotoSorting()

        demoSortingPage.click_multiple_lists_tab()

        # demoSortingPage.multiple_lists_drag_and_drop_to_sort("Item 2", "sortable1", "Item 4", "sortable2")
        # time.sleep(3)
        # demoSortingPage.multiple_lists_drag_and_drop_to_sort("Item 4", "sortable1", "Item 1", "sortable2")
        # time.sleep(3)
        # demoSortingPage.multiple_lists_drag_and_drop_to_sort("Item 5", "sortable2", "Item 1", "sortable1")
        # time.sleep(3)

        demoSortingPage.multiple_lists_drag_and_drop_to_sort("Item 2", "sortable2", "Item 3", "sortable1")


        # Define the expected order for each list after the move
        expected_order_list1 = ["Item 1", "Item 2", "Item 3", "Item 2", "Item 4", "Item 5"]
        expected_order_list2 = ["Item 1", "Item 3", "Item 4", "Item 5"]

        # Verify the order of both lists
        demoSortingPage.verify_multiple_lists_order("sortable1", expected_order_list1)
        demoSortingPage.verify_multiple_lists_order("sortable2", expected_order_list2)

        time.sleep(10)



    def test_simple_list_drag_drop(self):
        """
        Verifies that clicking the 'Start Download' button makes the
        file download dialog box appear.
        """

        # Instantiate page objects
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoSortingPage = demoPage.gotoSorting()

        demoSortingPage.click_simple_list_tab()

        start_item = "Item 6"
        end_item = "Item 4"
        # Call the method
        demoSortingPage.simple_list_drag_and_drop_to_sort(start_text=start_item, end_text=end_item)
        time.sleep(6)
        expected_order = ["Item 1", "Item 2", "Item 3", "Item 6", "Item 4", "Item 5", "Item 7"]
        demoSortingPage.verify_simple_list_order(expected_order)


    def test_grid_sorting(self):
        """
        Verifies that clicking the 'Start Download' button makes the
        file download dialog box appear.
        """

        # Instantiate page objects
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoSortingPage = demoPage.gotoSorting()

        demoSortingPage.click_grid_sorting_tab()

        start_item = "12"
        end_item = "11"
        # Call the method
        demoSortingPage.grid_sorting_drag_and_drop_to_sort(start_text=start_item, end_text=end_item)
        time.sleep(6)
        expected_order = ["1","2","3","4","5","6","7","8","9","10","12","11"]
        demoSortingPage.verify_grid_reorder_list_order(expected_order)
