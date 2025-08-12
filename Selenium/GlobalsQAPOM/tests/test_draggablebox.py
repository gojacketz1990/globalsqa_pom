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


