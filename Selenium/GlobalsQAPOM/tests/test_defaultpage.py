import pytest
import time
from pages.globalsqa_mainpage import GlobalsqaMainPage

@pytest.mark.usefixtures("setup_globalsqa")
class TestMethods():



    def test_gotoDemoPage(self):
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()
        demoTabsPage = demoPage.gotoTabs()
        success = demoTabsPage.expandSectionThree()
        assert success, "Accordion section three should expand"
        time.sleep(3)  # optional, better to wait dynamically



    def test_demoSliders(self):
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()
        demoSliderPage = demoPage.gotoSlider()
        demoSliderPage.move_slider_by_color("red",-25)
        demoSliderPage.move_slider_by_color("green",-15)
        demoSliderPage.move_slider_by_color("blue",-15)
        time.sleep(3)  # optional, better to wait dynamically

