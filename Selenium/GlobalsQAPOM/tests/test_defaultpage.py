import pytest
import time
from pages.globalsqa_mainpage import GlobalsqaMainPage

@pytest.mark.usefixtures("setup_globalsqa")
class TestMethods():



    # def test_gotoDemoPage(self):
    #     globalsqaPage = GlobalsqaMainPage(self.driver)
    #     demoPage = globalsqaPage.header.gotoDemoSitePage()
    #     demoTabsPage = demoPage.gotoTabs()
    #     success = demoTabsPage.expandSectionThree()
    #     assert success, "Accordion section three should expand"
    #     time.sleep(3)  # optional, better to wait dynamically
    #

    # def test_demoSliders(self):
    #         globalsqaPage = GlobalsqaMainPage(self.driver)
    #         demoPage = globalsqaPage.header.gotoDemoSitePage()
    #         demoSliderPage = demoPage.gotoSlider()
    #         demoSliderPage.move_slider_by_color("red",-25)
    #         demoSliderPage.move_slider_by_color("green",-15)
    #         demoSliderPage.move_slider_by_color("blue",-15)
    #         time.sleep(3)  # optional, better to wait dynamically


     def test_demoSliders(self):
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
            demoSliderPage.take_screenshot("slider_test.png")
