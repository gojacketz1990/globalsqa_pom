from pages.BasePage import BasePage
from pages.Header_Components import HeaderComponent
from locators.angularjs_searchfilter_locators import AngularJSSearchFilterPageLocators
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
import time
import datetime
import pytest
import re
import json

class AngularJSSearchFilterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.angularJSSearchFilterPageLocators = AngularJSSearchFilterPageLocators()


    def payee_search(self, text):
        self.type_into_element(text, AngularJSSearchFilterPageLocators.payee_search_box_locator)

    def account_search(self, account):
        self.select_from_dropdown_by_visible_text(AngularJSSearchFilterPageLocators.account_dropdown_locator, account)

    def search_by_type(self, type):
        self.select_from_dropdown_by_visible_text(AngularJSSearchFilterPageLocators.search_by_type_dropdown_locator, type)

    def search_by_expenditure_payee(self, payee):
        self.type_into_element(payee, AngularJSSearchFilterPageLocators.search_by_expenditure_payees_locator)

    def get_number_of_rows(self) -> int:
        """Returns the number of rows in the results table."""
        table_body = self.get_element(AngularJSSearchFilterPageLocators.results_table_body)
        rows = self.get_child_elements(table_body, AngularJSSearchFilterPageLocators.results_table_rows)
        return len(rows)

    def get_all_results_data(self) -> list:
        """Returns all data from the results table as a list of lists."""
        return self.read_table(
            AngularJSSearchFilterPageLocators.results_table_body,
            AngularJSSearchFilterPageLocators.results_table_rows,
            AngularJSSearchFilterPageLocators.results_table_cells
        )
