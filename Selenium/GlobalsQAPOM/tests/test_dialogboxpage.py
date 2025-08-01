import pytest
from pages.globalsqa_mainpage import GlobalsqaMainPage

@pytest.mark.usefixtures("setup_globalsqa")
class TestDialogBoxTabs:

    def test_message_box_tab_activation(self):
        """
        Verifies that the 'Message Box' tab becomes active when clicked.
        """
        print(f"\nTesting activation of the 'message_box_tab' tab...")

        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()
        demoDialogBoxPage = demoPage.gotoDialogBox()

        # Call the generic verification method with the specific tab name
        demoDialogBoxPage.verify_tab_becomes_active_by_name("message_box_tab")

    def test_confirmation_tab_activation(self):
        """
        Verifies that the 'Confirmation' tab becomes active when clicked.
        """
        print(f"\nTesting activation of the 'confirmation_tab' tab...")

        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()
        demoDialogBoxPage = demoPage.gotoDialogBox()

        # Call the generic verification method with the specific tab name
        demoDialogBoxPage.verify_tab_becomes_active_by_name("confirmation_tab")

    def test_form_tab_activation(self):
        """
        Verifies that the 'Form' tab becomes active when clicked.
        """
        print(f"\nTesting activation of the 'form_tab' tab...")

        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()
        demoDialogBoxPage = demoPage.gotoDialogBox()

        # Call the generic verification method with the specific tab name
        demoDialogBoxPage.verify_tab_becomes_active_by_name("form_tab")
