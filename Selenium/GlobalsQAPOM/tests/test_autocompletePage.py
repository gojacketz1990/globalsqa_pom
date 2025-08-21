
import pytest
from pages.globalsqa_mainpage import GlobalsqaMainPage
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

@pytest.mark.usefixtures("setup_globalsqa")
class TestDropdown:

    def test_categories_autocomplete_appears_on_typing(self):
        # Instantiate page objects
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoAutocompletePage = demoPage.gotoAutocomplete()

        demoAutocompletePage.enter_text_into_search("a")
        try:
            # --- 3. Assertion ---
            suggestions = demoAutocompletePage.get_autocomplete_suggestions()
            assert len(suggestions) > 0, "No suggestions appeared after typing 'a'."
            demoAutocompletePage.logger.info(f"✅ PASS: {len(suggestions)} suggestions appeared after typing 'a'.")

        except (NoSuchElementException, TimeoutException) as e:
            demoAutocompletePage.logger.error(f"❌ FAIL: An error occurred during test: {e}")




    def test_categories_selecting_suggestions_after_input(self):
        # Instantiate page objects
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoAutocompletePage = demoPage.gotoAutocomplete()

        demoAutocompletePage.enter_text_into_search("and")
        expected_text = "andreas andersson"
        demoAutocompletePage.select_suggestion_by_text(expected_text)

        input_value = demoAutocompletePage.get_search_input_value()

        assert input_value == expected_text, \
            f"Expected input value to be '{expected_text}' but found '{input_value}'."


    def test_correct_number_of_suggestions_and_categories_ignored(self):
        """
        Verifies that only the clickable suggestions are found,
        and the category headers are correctly ignored by the locator.
        Based on the provided HTML, typing 'a' should show 9 clickable items.
        """
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoAutocompletePage = demoPage.gotoAutocomplete()

        demoAutocompletePage.enter_text_into_search("and")
        time.sleep(3)
        # --- 3. Assertion ---
        suggestions = demoAutocompletePage.get_autocomplete_suggestions()
        expected_suggestions_count = 5
        assert len(suggestions) == expected_suggestions_count, \
            f"Expected {expected_suggestions_count} suggestions but found {len(suggestions)}."


    def test_combobox_autocomplete_appears_on_typing(self):
        # Instantiate page objects
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoAutocompletePage = demoPage.gotoAutocomplete()

        demoAutocompletePage.enter_text_combobox_search("j")
        time.sleep(3)
        try:
            # --- 3. Assertion ---
            suggestions = demoAutocompletePage.get_combobox_suggestions()
            assert len(suggestions) > 0, "No suggestions appeared after typing 'j'."
            demoAutocompletePage.logger.info(f"✅ PASS: {len(suggestions)} suggestions appeared after typing 'a'.")

        except (NoSuchElementException, TimeoutException) as e:
            demoAutocompletePage.logger.error(f"❌ FAIL: An error occurred during test: {e}")



    def test_combobox_selecting_suggestions_after_input(self):
        # Instantiate page objects
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoAutocompletePage = demoPage.gotoAutocomplete()

        demoAutocompletePage.enter_text_combobox_search("ja")
        expected_text = "JavaScript"
        demoAutocompletePage.select_combobox_suggestion_by_text(expected_text)

        time.sleep(3)

        input_value = demoAutocompletePage.get_combobox_input_value()

        assert input_value == expected_text, \
            f"Expected input value to be '{expected_text}' but found '{input_value}'."


    def test_combobox_correct_number_of_suggestions(self):
        """
        Verifies that only the clickable suggestions are found,
        and the category headers are correctly ignored by the locator.
        Based on the provided HTML, typing 'a' should show 9 clickable items.
        """
        globalsqaPage = GlobalsqaMainPage(self.driver)
        demoPage = globalsqaPage.header.gotoDemoSitePage()

        # Step 1: Click the "Message Box" tab to reveal the download button
        demoAutocompletePage = demoPage.gotoAutocomplete()

        demoAutocompletePage.enter_text_combobox_search("j")

        # --- 3. Assertion ---
        suggestions = demoAutocompletePage.get_combobox_suggestions()
        expected_suggestions_count = 3
        assert len(suggestions) == expected_suggestions_count, \
            f"Expected {expected_suggestions_count} suggestions but found {len(suggestions)}."
