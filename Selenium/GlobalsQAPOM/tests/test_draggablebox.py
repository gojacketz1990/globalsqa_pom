import pytest
from pages.globalsqa_mainpage import GlobalsqaMainPage
import time

@pytest.mark.usefixtures("setup_globalsqa")
class TestDraggableBox:


    def test_draggable_box_moves_freely(self):
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoDraggableBoxPage = demoPage.gotoDraggableBox()
        demoDraggableBoxPage.click_simpledrag_tab()
        initial_position = demoDraggableBoxPage.get_draggable_box_position()
        initial_x = initial_position['x']
        initial_y = initial_position['y']

        # Define the offset for the drag (e.g., move 50 pixels right, 30 pixels down)
        x_offset = 150
        y_offset = 130

        # 2. Perform the drag action
        demoDraggableBoxPage.drag_box_by_offset(x_offset, y_offset)

        # 3. Get the final position of the draggable box
        final_position = demoDraggableBoxPage.get_draggable_box_position()
        final_x = final_position['x']
        final_y = final_position['y']

        # 4. Assert that the box moved by the expected offset
        # Allow for a small tolerance due to potential browser rendering differences
        tolerance = 2

        assert abs(final_x - (initial_x + x_offset)) <= tolerance, \
            f"Expected X position {initial_x + x_offset} (with tolerance {tolerance}), but got {final_x}"
        assert abs(final_y - (initial_y + y_offset)) <= tolerance, \
            f"Expected Y position {initial_y + y_offset} (with tolerance {tolerance}), but got {final_y}"

        time.sleep(5)


    def test_check_events_drag_and_drop(self):
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoDraggableBoxPage = demoPage.gotoDraggableBox()
        demoDraggableBoxPage.click_checkevents_tab()

        # 1. Get initial event counts
        initial_start_count = demoDraggableBoxPage.get_check_event_count('start')
        initial_drag_count = demoDraggableBoxPage.get_check_event_count('drag')
        initial_stop_count = demoDraggableBoxPage.get_check_event_count('stop')

        # 2. Perform the drag action
        x_offset = 50
        y_offset = 50
        demoDraggableBoxPage.drag_check_events_draggable_box(x_offset, y_offset)

        # 3. Get final event counts
        final_start_count = demoDraggableBoxPage.get_check_event_count('start')
        final_drag_count = demoDraggableBoxPage.get_check_event_count('drag')
        final_stop_count = demoDraggableBoxPage.get_check_event_count('stop')

        # 4. Assertions
        # The 'start' event should have been invoked exactly once.
        assert final_start_count == initial_start_count + 1, \
            f"Expected start count to be {initial_start_count + 1}, but got {final_start_count}"

        # The 'drag' event should have been invoked multiple times (more than the initial count).
        assert final_drag_count > initial_drag_count, \
            f"Expected drag count ({final_drag_count}) to be greater than initial count ({initial_drag_count})"

        # The 'stop' event should have been invoked exactly once.
        assert final_stop_count == initial_stop_count + 1, \
            f"Expected stop count to be {initial_stop_count + 1}, but got {final_stop_count}"


    def test_handle_drag_and_drop(self):
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoDraggableBoxPage = demoPage.gotoDraggableBox()
        demoDraggableBoxPage.click_handle_tab()
        x_offset, y_offset = 50, 50

        # Test 1: Verify the handle is draggable
        # -------------------------------------
        initial_handle_position = demoDraggableBoxPage.get_first_handle_element_position()
        demoDraggableBoxPage.drag_first_handle_element_by_offset(x_offset, y_offset)
        final_handle_position = demoDraggableBoxPage.get_first_handle_element_position()

        # Assert that the position has changed
        assert final_handle_position['x'] != initial_handle_position['x'], "Handle drag failed: X position did not change."
        assert final_handle_position['y'] != initial_handle_position['y'], "Handle drag failed: Y position did not change."

        # Test 2: Verify the container is NOT draggable
        # ---------------------------------------------
        # Get the position again after the first drag
        initial_container_position = demoDraggableBoxPage.get_first_container_element_position()
        demoDraggableBoxPage.drag_first_container_element_by_offset(x_offset, y_offset)
        final_container_position = demoDraggableBoxPage.get_first_container_element_position()

        # Assert that the position has NOT changed
        assert final_container_position['x'] == initial_container_position['x'], "Container drag succeeded unexpectedly."
        assert final_container_position['y'] == initial_container_position['y'], "Container drag succeeded unexpectedly."

    def test_vertical_constraints_drag_and_drop(self):
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoDraggableBoxPage = demoPage.gotoDraggableBox()
        demoDraggableBoxPage.click_constraints_tab()


        # Define a small tolerance for floating point comparisons if necessary
        # (e.g., due to browser rendering or minor pixel shifts)
        tolerance = 2

        # --- Test 1: Vertical Movement ---

        initial_pos_vertical_test = demoDraggableBoxPage.get_vertical_draggable_box_position()
        print(initial_pos_vertical_test)

        # Drag vertically (0 x-offset, 50 y-offset)
        vertical_move_y_offset = 50
        demoDraggableBoxPage.drag_vertical_draggable_box_by_offset(0, vertical_move_y_offset)

        final_pos_vertical_test = demoDraggableBoxPage.get_vertical_draggable_box_position()
        print(final_pos_vertical_test)

        # Assert Y-coordinate changed by the expected amount
        assert abs(final_pos_vertical_test['y'] - (initial_pos_vertical_test['y'] + vertical_move_y_offset)) <= tolerance, \
            f"Expected Y position to change to {initial_pos_vertical_test['y'] + vertical_move_y_offset}, but got {final_pos_vertical_test['y']}"


        # Assert X-coordinate remained constant
        assert abs(final_pos_vertical_test['x'] - initial_pos_vertical_test['x']) <= tolerance, \
            f"Expected X position to remain constant ({initial_pos_vertical_test['x']}), but it changed to {final_pos_vertical_test['x']}"




        # --- Test 2: Horizontal Restriction ---

        # Get current position after the vertical drag (or re-get from page for isolation)
        initial_pos_horizontal_test = demoDraggableBoxPage.get_vertical_draggable_box_position()

        # Attempt to drag horizontally (50 x-offset, 0 y-offset)
        horizontal_move_x_offset = 50
        demoDraggableBoxPage.drag_vertical_draggable_box_by_offset(horizontal_move_x_offset, 0)

        final_pos_horizontal_test = demoDraggableBoxPage.get_vertical_draggable_box_position()

        # Assert X-coordinate did NOT change
        assert abs(final_pos_horizontal_test['x'] - initial_pos_horizontal_test['x']) <= tolerance, \
            f"Expected X position to remain constant ({initial_pos_horizontal_test['x']}), but it changed to {final_pos_horizontal_test['x']}"

        # Assert Y-coordinate did NOT change (since only horizontal movement was attempted)
        assert abs(final_pos_horizontal_test['y'] - initial_pos_horizontal_test['y']) <= tolerance, \
            f"Expected Y position to remain constant ({initial_pos_horizontal_test['y']}), but it changed to {final_pos_horizontal_test['y']}"

