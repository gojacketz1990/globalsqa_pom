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
        username = (firstname + lastname).lower()
        #username = data_generator.generate_username()
        password = data_generator.generate_strong_password()

        #print(firstname, lastname, username, password)

        
