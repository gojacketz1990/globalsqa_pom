from pages.BasePage import BasePage
from pages.Header_Components import HeaderComponent
from locators.angularjs_uploadimage_locators import AngularJSUploadImagePageLocators
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
import time
import datetime
import pytest
import re
import json

class AngularJSUploadImagePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.angularJSUploadImagePageLocators = AngularJSUploadImagePageLocators()

    def upload_file_path(self, filePath):
       self.upload_file(AngularJSUploadImagePageLocators.choose_file_button_locator,filePath)

    def get_upload_progress_value(self) -> str:
        """
        Retrieves the 'value' attribute from the progress bar element.
        """
        # Locate the progress element using its locator.
        progress_element = self.get_element(AngularJSUploadImagePageLocators.progress_bar)

        # Directly get the attribute from the located element.
        progress_value = progress_element.get_attribute("value")

        return progress_value
