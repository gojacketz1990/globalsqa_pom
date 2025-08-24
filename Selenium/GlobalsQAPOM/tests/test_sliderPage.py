import pytest
import time
from pages.globalsqa_mainpage import GlobalsqaMainPage
from utilities.LoggerBase import LoggerBase

@pytest.mark.usefixtures("setup_globalsqa")
class TestSliderPage(LoggerBase):


   def test_demoSliders(self, logger):
            globalsqaPage = GlobalsqaMainPage(self.driver)
            demoPage = globalsqaPage.header.gotoDemoSitePage()
            demoSliderPage = demoPage.gotoSlider()

            # Move sliders
            demoSliderPage.move_slider_by_color("red", -425)
            demoSliderPage.move_slider_by_color("green", -15)
            demoSliderPage.move_slider_by_color("blue", -15)

            # ✅ Add assertions
            red_pos = demoSliderPage.get_slider_handle_position("red")
            green_pos = demoSliderPage.get_slider_handle_position("green")
            blue_pos = demoSliderPage.get_slider_handle_position("blue")

            assert red_pos is not None, "Red slider handle position not found"
            assert green_pos is not None, "Green slider handle position not found"
            assert blue_pos is not None, "Blue slider handle position not found"

            # Example: check the sliders actually moved leftwards (e.g., <50%)
            assert red_pos < 50, f"Expected red slider to be less than 50%, got {red_pos}"
            assert green_pos < 50, f"Expected green slider to be less than 50%, got {green_pos}"
            assert blue_pos < 50, f"Expected blue slider to be less than 50%, got {blue_pos}"

            # optional visual check
