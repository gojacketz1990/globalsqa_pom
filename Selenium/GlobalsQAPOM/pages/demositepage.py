from pages.BasePage import BasePage
from pages.Header_Components import HeaderComponent
from locators.demosite_page_locators import DemoSitePageLocators
import time

class DemoPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.demoSitePageLocators = DemoSitePageLocators()

    def gotoTabs(self):
        from pages.demosite_TabsPage import DemoTabsPage
        self.element_click(self.demoSitePageLocators.tabs_locator)
        return DemoTabsPage(self.driver)


    def gotoSlider(self):
        from pages.demosite_SliderPage import DemoSliderPage
        self.element_click(self.demoSitePageLocators.slider_locator)
        return DemoSliderPage(self.driver)

    def gotoToolTip(self):
        from pages.demosite_ToolTipPage import DemoToolTipPage
        self.element_click(self.demoSitePageLocators.tooltip_locator)
        return DemoToolTipPage(self.driver)

    def gotoAlertBox(self):
        from pages.demosite_AlertBoxPage import DemoAlertBoxPage
        self.element_click(self.demoSitePageLocators.tooltip_locator)
        return DemoAlertBoxPage(self.driver)

    def gotoDialogBox(self):
        from pages.demosite_DialogBoxPage import DemoDialogBoxPage
        self.element_click(self.demoSitePageLocators.dialogbox_locator)
        return DemoDialogBoxPage(self.driver)

    def gotoProgressBar(self):
        from pages.demosite_ProgressBarPage import DemoProgressBarPage
        self.element_click(self.demoSitePageLocators.progressbar_locator)
        return DemoProgressBarPage(self.driver)

    def gotoFrames(self):
        from pages.demosite_FramesPage import DemoFramesPage
        self.element_click(self.demoSitePageLocators.frames_locator)
        return DemoFramesPage(self.driver)

    def gotoDropdown(self):
        from pages.demosite_DropDownPage import DemoDropDownPage
        self.element_click(self.demoSitePageLocators.dropdown_locator)
        return DemoDropDownPage(self.driver)

    def gotoAutocomplete(self):
        from pages.demosite_AutocompletePage import DemoAutocompletePage
        self.element_click(self.demoSitePageLocators.autocomplete_locator)
        return DemoAutocompletePage(self.driver)

    def gotoSelectElements(self):
        from pages.demosite_SelectElementsPage import DemoSelectElementsPage
        self.element_click(self.demoSitePageLocators.selectelements_locator)
        return DemoSelectElementsPage(self.driver)

    def gotoSorting(self):
        from pages.demosite_SortingPage import DemoSortingPage
        self.element_click(self.demoSitePageLocators.sorting_locator)
        return DemoSortingPage(self.driver)


    def gotoSpinner(self):
        from pages.demosite_SpinnerPage import DemoSpinnerPage
        self.element_click(self.demoSitePageLocators.spinner_locator)
        return DemoSpinnerPage(self.driver)

    def gotoToolBar(self):
        from pages.demosite_ToolbarPage import DemoToolBarPage
        self.element_click(self.demoSitePageLocators.toolbar_locator)
        return DemoToolBarPage(self.driver)

    def gotoDatePicker(self):

        from pages.demosite_DatePickerPage import DemoDatePickerPage
        self.scroll_to_element(self.demoSitePageLocators.datepicker_locator)
        self.element_click(self.demoSitePageLocators.datepicker_locator)
        return DemoDatePickerPage(self.driver)

    def gotoDragDrop(self):

        from pages.demosite_DragDropPage import DemoDragDropPage
        self.scroll_to_element(self.demoSitePageLocators.dragdrop_locator)
        self.element_click(self.demoSitePageLocators.dragdrop_locator)
        return DemoDragDropPage(self.driver)

    def gotoDraggableBox(self):

        from pages.demosite_DraggableBoxPage import DemoDraggableBoxPage
        self.scroll_to_element(self.demoSitePageLocators.draggable_box_locator)
        self.element_click(self.demoSitePageLocators.draggable_box_locator)
        return DemoDraggableBoxPage(self.driver)

    def gotoSamplePage(self):

        from pages.demosite_SamplePage import DemoSamplePage
        self.scroll_to_element(self.demoSitePageLocators.sample_page_locator)
        self.element_click(self.demoSitePageLocators.sample_page_locator)
        return DemoSamplePage(self.driver)

