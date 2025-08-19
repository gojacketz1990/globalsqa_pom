from pages.BasePage import BasePage
from pages.Header_Components import HeaderComponent
from locators.angularjs_bankingproject_locators import AngularJSBankingProjectPageLocators
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
import time
import datetime
import pytest
import re
import json

class AngularJSBankingProjectPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.angularJSBankingProjectPageLocators = AngularJSBankingProjectPageLocators()

    def click_home_button(self):
        self.element_click(AngularJSBankingProjectPageLocators.home_button_locator)

    def click_customer_login_button(self):
        self.element_click(AngularJSBankingProjectPageLocators.customer_login_locator)

    def click_manager_login_button(self):
        self.element_click(AngularJSBankingProjectPageLocators.bank_manager_login_locator)

    def select_name_dropdown(self,name):
        self.select_from_dropdown_by_visible_text(AngularJSBankingProjectPageLocators.customer_name_dropdown_locator,name)

    def select_manager_dropdown(self,name):
        self.select_from_dropdown_by_visible_text(AngularJSBankingProjectPageLocators.bank_manager_login_locator,name)

    def click_login_button(self):
        self.element_click(AngularJSBankingProjectPageLocators.login_button_locator)
