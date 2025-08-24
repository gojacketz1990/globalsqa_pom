import pytest
from pages.globalsqa_mainpage import GlobalsqaMainPage
import time
from utilities.LoggerBase import LoggerBase

@pytest.mark.usefixtures("setup_globalsqa")
class TestDragAndDrop(LoggerBase):

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
        demoDragDropPage.select_items_with_drag_and_drop(item_to_drag)

        # Assertion 1: The item should now be in the trash
        assert demoDragDropPage.is_item_in_trash(item_to_drag), \
            f"Item '{item_to_drag}' was not found in the trash."

        # Assertion 2: The item should no longer be in the gallery
        assert not demoDragDropPage.is_item_in_gallery(item_to_drag), \
            f"Item '{item_to_drag}' was unexpectedly found in the original gallery."




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
        demoDragDropPage.drag_and_drop_invalid_item_to_trash()

        # Assertion 1: The droppable area's class has not changed
        assert demoDragDropPage.is_droppable_item_unchanged() is True, \
            "The droppable area changed state, indicating an invalid drop was accepted."

        # Assertion 2: The text of the droppable area has not changed
        final_text = demoDragDropPage.get_droppable_text()
        assert initial_text == final_text, \
            "The text of the droppable area changed, indicating an invalid drop was accepted."


    def test_droppable_item_can_be_dropped(self):

        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoDragDropPage = demoPage.gotoDragDrop()

        demoDragDropPage.click_accepted_elements_tab()

        # Get the initial state of the droppable area for comparison
        initial_text = demoDragDropPage.get_droppable_text()

        # Perform the drag and drop of the non-valid item
        demoDragDropPage.drag_and_drop_valid_item_to_trash()

        # Assertion 1: The droppable area's class has not changed
        assert demoDragDropPage.is_droppable_item_unchanged() is False, \
            "The droppable area changed state, indicating a valid drop was accepted."

        # Assertion 2: The text of the droppable area has not changed
        final_text = demoDragDropPage.get_droppable_text()
        assert final_text == "Dropped!", \
            "The text of the droppable area changed, indicating an invalid drop was accepted."


    #Drop in greedy not set, both the folder and sub folder register as dropped
    #On greedy, only the one you are over registered as dropped
    #Test - drag droppable to drop area, make sure text changes

    #Four paths - not greedy outer, not greedy inner, greedy outer, greedy inner
    #not greedy outer - outer becomes dropped, not greedy inner - both become dropped
    #greedy outer - outer becomes dropped
    #greedy inner - inner becomes dropped

    def test_propagation(self):

        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoDragDropPage = demoPage.gotoDragDrop()

        demoDragDropPage.click_propagation_tab()

    def test_outer_not_greedy(self):
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoDragDropPage = demoPage.gotoDragDrop()

        demoDragDropPage.click_propagation_tab()

    def test_inner_not_greedy(self):
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoDragDropPage = demoPage.gotoDragDrop()

        demoDragDropPage.click_propagation_tab()

    def test_outer_greedy(self):
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoDragDropPage = demoPage.gotoDragDrop()

        demoDragDropPage.click_propagation_tab()

    def test_inner_nongreedy(self):
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoDragDropPage = demoPage.gotoDragDrop()

        demoDragDropPage.click_propagation_tab()

        # 1. Get initial text for verification
        initial_inner_text = demoDragDropPage.get_text_of_droppable_area("inner_nongreedy")
        initial_outer_text = demoDragDropPage.get_text_of_droppable_area("outer_nongreedy")

        # 2. Perform the drag-and-drop
        demoDragDropPage.drag_propagation_item_to_target("inner_nongreedy")
        time.sleep(5)
        # 3. Get the final text
        final_inner_text = demoDragDropPage.get_text_of_droppable_area("inner_nongreedy")
        final_outer_text = demoDragDropPage.get_text_of_droppable_area("outer_nongreedy")

        # 4. Assertions
        assert final_inner_text == "Dropped!", "Inner non-greedy box text did not change to 'Dropped!'."
        assert final_outer_text == "Dropped!", "Outer non-greedy box text did not change to 'Dropped!'."

        time.sleep(5)

    def test_outer_nongreedy(self):
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoDragDropPage = demoPage.gotoDragDrop()

        demoDragDropPage.click_propagation_tab()

        # 1. Get initial text for verification
        initial_inner_text = demoDragDropPage.get_text_of_droppable_area("inner_nongreedy")
        initial_outer_text = demoDragDropPage.get_text_of_droppable_area("outer_nongreedy")

        # 2. Perform the drag-and-drop
        demoDragDropPage.drag_propagation_item_to_target("outer_nongreedy")
        time.sleep(5)
        # 3. Get the final text
        final_inner_text = demoDragDropPage.get_text_of_droppable_area("inner_nongreedy")
        final_outer_text = demoDragDropPage.get_text_of_droppable_area("outer_nongreedy")

        # 4. Assertions
        assert final_inner_text == initial_inner_text, "Outer non-greedy box text should not have changed."
        assert final_outer_text == "Dropped!", "Outer non-greedy box text did not change to 'Dropped!'."

        time.sleep(5)

    def test_inner_greedy(self):
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoDragDropPage = demoPage.gotoDragDrop()

        demoDragDropPage.click_propagation_tab()

        # 1. Get initial text for verification
        initial_inner_text = demoDragDropPage.get_text_of_droppable_area("inner_greedy")
        initial_outer_text = demoDragDropPage.get_text_of_droppable_area("outer_greedy")

        # 2. Perform the drag-and-drop
        demoDragDropPage.drag_propagation_item_to_target("inner_greedy")
        time.sleep(5)
        # 3. Get the final text
        final_inner_text = demoDragDropPage.get_text_of_droppable_area("inner_greedy")
        final_outer_text = demoDragDropPage.get_text_of_droppable_area("outer_greedy")

        # 4. Assertions
        assert final_inner_text == "Dropped!", "Inner greedy box text did not change to 'Dropped!'."
        assert final_outer_text == initial_outer_text, "Outer greedy box text should not have changed."

        time.sleep(5)



    def test_outer_greedy(self):
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoDragDropPage = demoPage.gotoDragDrop()

        demoDragDropPage.click_propagation_tab()

        # 1. Get initial text for verification
        initial_inner_text = demoDragDropPage.get_text_of_droppable_area("inner_greedy")
        initial_outer_text = demoDragDropPage.get_text_of_droppable_area("outer_greedy")

        # 2. Perform the drag-and-drop
        demoDragDropPage.drag_propagation_item_to_target("outer_greedy")
        time.sleep(5)
        # 3. Get the final text
        final_inner_text = demoDragDropPage.get_text_of_droppable_area("inner_greedy")
        final_outer_text = demoDragDropPage.get_text_of_droppable_area("outer_greedy")

        # 4. Assertions
        assert final_inner_text == initial_inner_text, "Inner greedy box text should not hve changed!'."
        assert final_outer_text == "Dropped!", "Outer greedy box text did not change to 'Dropped!'."

        time.sleep(5)
