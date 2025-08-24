import pytest
import time
from pages.globalsqa_mainpage import GlobalsqaMainPage
from utilities.LoggerBase import LoggerBase

@pytest.mark.usefixtures("setup_globalsqa")
class TestToolTips:
    def test_visible_tooltips_display_correct_text(self):
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()
        demoToolTipPage = demoPage.gotoToolTip()

        text = demoToolTipPage.hover_and_get_visible_tooltip_text(
            demoToolTipPage.demoToolTipPageLocators.st_stephens_img_locator)
        print("Visible St. Stephen's tooltip:", text)
        assert "St. Stephen" in text

        text = demoToolTipPage.hover_and_get_visible_tooltip_text(
            demoToolTipPage.demoToolTipPageLocators.tower_bridge_img_locator)
        print("Visible Tower Bridge tooltip:", text)
        assert "Tower Bridge" in text

        # text = demoToolTipPage.hover_and_get_visible_tooltip_text(
        #     demoToolTipPage.demoToolTipPageLocators.london_link_locator)
        # print("Visible London tooltip:", text)
        # assert "London" in text

        text = demoToolTipPage.hover_and_get_visible_tooltip_text(
            demoToolTipPage.demoToolTipPageLocators.cc_link_locator)
        print("Visible CC tooltip:", text)
        assert "Creative Commons" in text

        demoToolTipPage.take_screenshot("visible_tooltips_test.png")
        time.sleep(2)
