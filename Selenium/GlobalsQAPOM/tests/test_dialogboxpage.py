import pytest
from pages.globalsqa_mainpage import GlobalsqaMainPage

@pytest.mark.usefixtures("setup_globalsqa")
class TestDialogBoxTabs:

    def test_confirmation_box_cancel(self):
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()
        demoDialogBoxPage = demoPage.gotoDialogBox()
        demoDialogBoxPage.click_confirmation_tab()
        demoDialogBoxPage.confirm_cancel_delete()

        assert not demoDialogBoxPage.is_empty_recycle_bin_present(), \
            "FAIL: The confirmation dialog box did not disappear after clicking 'OK'."


    def test_confirmation_box_delete_all(self):
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()
        demoDialogBoxPage = demoPage.gotoDialogBox()
        demoDialogBoxPage.click_confirmation_tab()
        demoDialogBoxPage.confirm_delete_all_items()

        assert not demoDialogBoxPage.is_empty_recycle_bin_present(), \
            "FAIL: The confirmation dialog box did not disappear after clicking 'OK'."

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



    def test_read_user_table(self):
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()
        demoDialogBoxPage = demoPage.gotoDialogBox()

        demoDialogBoxPage.click_form_tab()
        # This single call gets all the data
        all_users_data = demoDialogBoxPage.get_all_users_data()


        if all_users_data:
            # Print the header row
            header = all_users_data[0]
            print(f"{header[0]:<15} {header[1]:<25} {header[2]:<10}")
            print("-" * 52) # Print a separator line

            # Print the data rows, skipping the header
            for user_data in all_users_data[0:]:
                name, email, password = user_data
                print(f"Name: {name:<15} email: {email:<25} password:{password:<10}")

    def create_user_and_verify(self):

        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()
        demoDialogBoxPage = demoPage.gotoDialogBox()

        demoDialogBoxPage.click_form_tab()
        demoDialogBoxPage.create_new_user("Matt Adams", "gojacketz@ireapit.com","passingword")

    def test_create_user_and_verify(self):
        # Test Data
        new_user_name = "Matt Adams"
        new_user_email = "gojacketz@ireapit.com"
        new_user_password = "passingword"

        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()
        demoDialogBoxPage = demoPage.gotoDialogBox()

        demoDialogBoxPage.verify_tab_becomes_active_by_name("form_tab")

        # Step 1: Get the current user data before creating the new user
        initial_users_data = demoDialogBoxPage.get_all_users_data()
        initial_user_count = len(initial_users_data)

        # Step 2: Create the new user
        demoDialogBoxPage.create_new_user(new_user_name, new_user_email, new_user_password)

        # Step 3: Get the user data again after creating the new user
        updated_users_data = demoDialogBoxPage.get_all_users_data()
        updated_user_count = len(updated_users_data)

        # Step 4: Add the assertions

        # Assertion 1: Verify the number of users has increased by one
        assert updated_user_count == initial_user_count + 1, "The new user was not added to the table."

        # Assertion 2: Verify the new user's data exists in the updated table
        # We can create a list representing the new user's data
        new_user_data = [new_user_name, new_user_email, new_user_password]

        # Use a simple 'in' check to see if the new user's data is in the list of all users
        assert new_user_data in updated_users_data, f"New user {new_user_name} not found in the table."

        # Optional: You can also print the data to see the result
        print("User created successfully. Final user table:")
        print(updated_users_data)

    def test_downloadcomplete_check_percentage(self):
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()
        demoDialogBoxPage = demoPage.gotoDialogBox()

        demoDialogBoxPage.click_message_box_tab()

        storage_message = demoDialogBoxPage.get_storage_percentage()

        # Print the result
        print("The storage message is:")
        print(storage_message)

        assert demoDialogBoxPage.is_download_dialog_present(), "Download complete dialog was not displayed."
        #
        # # Step 2: Check the storage percentage
        # # Note: You can use a more dynamic check if the number changes
        storage_percentage = demoDialogBoxPage.get_storage_percentage()
        assert storage_percentage == 36, f"Expected storage percentage to be 36, but got {storage_percentage}"

        # assert storage_percentage == 36, f"Expected 36% storage, but got {storage_percentage}%."
        #
        # # Step 3: Click the "Ok" button
        # demoDialogBoxPage.click_ok_on_dialog()
        #
        # # Optional: Assert the dialog is no longer present after clicking OK
        # assert not demoPage.is_element_present(demoDialogBoxPage._dialog_locator), "Dialog did not close after clicking Ok."


    def test_downloadcomplete_click_ok(self):
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()
        demoDialogBoxPage = demoPage.gotoDialogBox()

        demoDialogBoxPage.click_message_box_tab()

        demoDialogBoxPage.click_ok_download_complete()
        assert not demoDialogBoxPage.is_download_dialog_present(), \
            "FAIL: The confirmation dialog box did not disappear after clicking 'OK'."
