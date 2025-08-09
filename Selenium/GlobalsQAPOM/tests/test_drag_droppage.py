import pytest
from pages.globalsqa_mainpage import GlobalsqaMainPage
import time

@pytest.mark.usefixtures("setup_globalsqa")
class TestDragAndDrop:

    def test_drag_and_drop(self):
        """
        Verifies that clicking the 'Start Download' button makes the
        file download dialog box appear.
        """        # Instantiate page objects
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoDragDropPage = demoPage.gotoDragDrop()

        #demoDragDropPage.click_propagation_tab()
        # time.sleep(1)
        # demoDragDropPage.click_accepted_elements_tab()
        # time.sleep(1)
        demoDragDropPage.click_photo_manager_tab()
        # time.sleep(1)

        demoDragDropPage.select_items_with_drag_and_drop("High Tatras")

        time.sleep(3)

    def test_move_item_to_trash(self):
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoDragDropPage = demoPage.gotoDragDrop()

        #demoDragDropPage.click_propagation_tab()
        # time.sleep(1)
        # demoDragDropPage.click_accepted_elements_tab()
        # time.sleep(1)
        demoDragDropPage.click_photo_manager_tab()

        item_to_drag = "High Tatras"

        # Drag and drop the item (you would have a method for this)
        demoDragDropPage.drag_item_to_trash(item_to_drag)

        # Assertion 1: The item should now be in the trash
        assert demoDragDropPage.is_item_in_trash(item_to_drag), \
            f"Item '{item_to_drag}' was not found in the trash."

        # Assertion 2: The item should no longer be in the gallery
        assert not demoDragDropPage.is_item_in_gallery(item_to_drag), \
            f"Item '{item_to_drag}' was unexpectedly found in the original gallery."

    #Test - drag undroppable to drop area, make sure nothing changes in drop area
    #Drop in greedy not set, both the folder and sub folder register as dropped
    #On greedy, only the one you are over registered as dropped
    #Test - drag droppable to drop area, make sure text changes


    def test_accepted_elements(self):

        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoDragDropPage = demoPage.gotoDragDrop()

        #demoDragDropPage.click_propagation_tab()
        # time.sleep(1)
        # demoDragDropPage.click_accepted_elements_tab()
        # time.sleep(1)
        demoDragDropPage.click_accepted_elements_tab()


    def test_unaccepted_item_cannot_be_dropped(self):

        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoDragDropPage = demoPage.gotoDragDrop()

        demoDragDropPage.click_accepted_elements_tab()

        # Get the initial state of the droppable area for comparison
        initial_text = demoDragDropPage.get_droppable_text()

        # Perform the drag and drop of the non-valid item
        demoDragDropPage.drag_and_drop_nonvalid_item()

        # Assertion 1: The droppable area's class has not changed
        assert demoDragDropPage.is_droppable_item_unchanged() is True, \
            "The droppable area changed state, indicating an invalid drop was accepted."

        # Assertion 2: The text of the droppable area has not changed
        final_text = demoDragDropPage.get_droppable_text()
        assert initial_text == final_text, \
            "The text of the droppable area changed, indicating an invalid drop was accepted."
