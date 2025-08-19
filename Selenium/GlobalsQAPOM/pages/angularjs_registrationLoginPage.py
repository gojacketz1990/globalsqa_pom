from pages.BasePage import BasePage
from pages.Header_Components import HeaderComponent
from locators.angularjs_registration_login_locators import AngularJSRegistrationLoginPageLocators
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
import time
import datetime
import pytest
import re
import json

class AngularJSRegistrationLoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.angularJSRegistrationLoginPageLocators = AngularJSRegistrationLoginPageLocators()

    def enter_username(self, username):
        self.type_into_element(username, AngularJSRegistrationLoginPageLocators.username_locator)

    def enter_password(self, password):
        self.type_into_element(password, AngularJSRegistrationLoginPageLocators.password_locator)

    def click_login_button(self):
        self.element_click(AngularJSRegistrationLoginPageLocators.login_button_locator)


    def click_register_link(self):
        self.element_click(AngularJSRegistrationLoginPageLocators.register_link_locator)

    def register_enter_first_name(self, firstname):
        self.type_into_element(firstname, AngularJSRegistrationLoginPageLocators.register_first_name_locator)

    def register_enter_last_name(self, lastname):
        self.type_into_element(lastname, AngularJSRegistrationLoginPageLocators.register_last_name_locator)

    def register_enter_username(self, username):
        self.type_into_element(username, AngularJSRegistrationLoginPageLocators.register_username_locator)

    def register_enter_password(self, password):
        self.type_into_element(password, AngularJSRegistrationLoginPageLocators.register_password_locator)

    def click_register_button(self):
        self.element_click(AngularJSRegistrationLoginPageLocators.register_button_locator)

    def click_cancel_registration_link(self):
        self.element_click(AngularJSRegistrationLoginPageLocators.cancel_link_locator)

    def is_registration_successful(self) -> bool:
        """Verifies that the registration successful message is displayed."""
        return self.is_text_present("Registration successful")

    def is_login_incorrect(self) -> bool:
        """Verifies that an incorrect login error message is displayed."""
        #print(self.is_text_present("Username or password is incorrect"))
        return self.is_text_present("Username or password is incorrect")

    def is_register_button_active(self) -> bool:
        """Verifies if the Register button is active (not disabled)."""
        # The absence of the 'disabled' attribute indicates the button is active.
        return self.get_element_attribute(AngularJSRegistrationLoginPageLocators.register_button_locator, "disabled") is None
