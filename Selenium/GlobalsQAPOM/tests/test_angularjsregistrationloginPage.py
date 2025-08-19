import pytest
from pages.globalsqa_mainpage import GlobalsqaMainPage
import time
from utilities.FakerHelper import FakerHelper

@pytest.mark.usefixtures("setup_globalsqa")
class TestRegistrationLogin:

    def test_registration(self):

        from utilities.FakerHelper import FakerHelper
        data_generator = FakerHelper(locale='en_US')

        globalsqaPage = GlobalsqaMainPage(self.driver)
        angularjsPage = globalsqaPage.header.gotoAngularSitePage()

        registrationloginPage = angularjsPage.gotoRegistrationLogin()

        time.sleep(3)

        registrationloginPage.click_register_link()

        firstname = data_generator.generate_first_name()
        lastname = data_generator.generate_last_name()
        username = (firstname + "." +lastname).lower()
        #username = data_generator.generate_username()
        password = data_generator.generate_strong_password()

        print(firstname, lastname, username, password)

        registrationloginPage.register_enter_first_name(firstname)
        registrationloginPage.register_enter_last_name(lastname)
        registrationloginPage.register_enter_username(username)
        registrationloginPage.register_enter_password(password)


        button_active = registrationloginPage.is_register_button_active()

        assert button_active, "The Register button is inactive, but should be active."

        registrationloginPage.click_register_button()

        registration_successful = registrationloginPage.is_registration_successful()

        assert registration_successful, "Registration was not successful; the success message was not found."


    def test_incorrect_login(self):

        from utilities.FakerHelper import FakerHelper
        data_generator = FakerHelper(locale='en_US')

        globalsqaPage = GlobalsqaMainPage(self.driver)
        angularjsPage = globalsqaPage.header.gotoAngularSitePage()

        registrationloginPage = angularjsPage.gotoRegistrationLogin()

        time.sleep(1)

        firstname = data_generator.generate_first_name()
        lastname = data_generator.generate_last_name()
        username = (firstname + "." +lastname).lower()
        #username = data_generator.generate_username()
        password = data_generator.generate_strong_password()

        print(firstname, lastname, username, password)

        registrationloginPage.enter_username(username)
        registrationloginPage.enter_password(password)

        registrationloginPage.click_login_button()


        login_unsuccessful = registrationloginPage.is_login_incorrect()

        assert login_unsuccessful, "Login was successful, but was expected to fail."

    def test_form_validation_no_first_name(self):

        from utilities.FakerHelper import FakerHelper
        data_generator = FakerHelper(locale='en_US')

        globalsqaPage = GlobalsqaMainPage(self.driver)
        angularjsPage = globalsqaPage.header.gotoAngularSitePage()

        registrationloginPage = angularjsPage.gotoRegistrationLogin()

        time.sleep(3)

        registrationloginPage.click_register_link()

        firstname = data_generator.generate_first_name()
        lastname = data_generator.generate_last_name()
        username = (firstname + "." +lastname).lower()
        #username = data_generator.generate_username()
        password = data_generator.generate_strong_password()

        print(firstname, lastname, username, password)

        #registrationloginPage.register_enter_first_name(firstname)
        registrationloginPage.register_enter_last_name(lastname)
        registrationloginPage.register_enter_username(username)
        registrationloginPage.register_enter_password(password)
        #registrationloginPage.click_register_button()


        button_active = registrationloginPage.is_register_button_active()

        assert not button_active, "The Register button is active, but should be inactive."

    def test_form_validation_no_last_name(self):

        from utilities.FakerHelper import FakerHelper
        data_generator = FakerHelper(locale='en_US')

        globalsqaPage = GlobalsqaMainPage(self.driver)
        angularjsPage = globalsqaPage.header.gotoAngularSitePage()

        registrationloginPage = angularjsPage.gotoRegistrationLogin()

        time.sleep(3)

        registrationloginPage.click_register_link()

        firstname = data_generator.generate_first_name()
        lastname = data_generator.generate_last_name()
        username = (firstname + "." +lastname).lower()
        #username = data_generator.generate_username()
        password = data_generator.generate_strong_password()

        print(firstname, lastname, username, password)

        registrationloginPage.register_enter_first_name(firstname)
        #registrationloginPage.register_enter_last_name(lastname)
        registrationloginPage.register_enter_username(username)
        registrationloginPage.register_enter_password(password)
        #registrationloginPage.click_register_button()


        button_active = registrationloginPage.is_register_button_active()

        assert not button_active, "The Register button is active, but should be inactive."

    def test_form_validation_no_username(self):

        from utilities.FakerHelper import FakerHelper
        data_generator = FakerHelper(locale='en_US')

        globalsqaPage = GlobalsqaMainPage(self.driver)
        angularjsPage = globalsqaPage.header.gotoAngularSitePage()

        registrationloginPage = angularjsPage.gotoRegistrationLogin()

        time.sleep(3)

        registrationloginPage.click_register_link()

        firstname = data_generator.generate_first_name()
        lastname = data_generator.generate_last_name()
        username = (firstname + "." +lastname).lower()
        #username = data_generator.generate_username()
        password = data_generator.generate_strong_password()

        print(firstname, lastname, username, password)

        registrationloginPage.register_enter_first_name(firstname)
        registrationloginPage.register_enter_last_name(lastname)
        #registrationloginPage.register_enter_username(username)
        registrationloginPage.register_enter_password(password)
        #registrationloginPage.click_register_button()


        button_active = registrationloginPage.is_register_button_active()

        assert not button_active, "The Register button is active, but should be inactive."

    def test_form_validation_no_password(self):

        from utilities.FakerHelper import FakerHelper
        data_generator = FakerHelper(locale='en_US')

        globalsqaPage = GlobalsqaMainPage(self.driver)
        angularjsPage = globalsqaPage.header.gotoAngularSitePage()

        registrationloginPage = angularjsPage.gotoRegistrationLogin()

        time.sleep(3)

        registrationloginPage.click_register_link()

        firstname = data_generator.generate_first_name()
        lastname = data_generator.generate_last_name()
        username = (firstname + "." +lastname).lower()
        #username = data_generator.generate_username()
        password = data_generator.generate_strong_password()

        print(firstname, lastname, username, password)

        registrationloginPage.register_enter_first_name(firstname)
        registrationloginPage.register_enter_last_name(lastname)
        registrationloginPage.register_enter_username(username)
        #registrationloginPage.register_enter_password(password)
        #registrationloginPage.click_register_button()

        time.sleep(1)
        button_active = registrationloginPage.is_register_button_active()

        assert not button_active, "The Register button is active, but should be inactive."
