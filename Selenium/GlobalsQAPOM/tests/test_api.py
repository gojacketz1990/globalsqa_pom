import pytest
from pages.globalsqa_mainpage import GlobalsqaMainPage
import time
from utilities.LoggerBase import LoggerBase
from utilities.FakerHelper import FakerHelper
from api_utils import addBook
from api_utils import getBook
import json

class TestAPI(LoggerBase):

    def test_api(self, logger):

        from utilities.FakerHelper import FakerHelper
        data_generator = FakerHelper(locale='en_US')


        firstname = data_generator.generate_first_name()
        lastname = data_generator.generate_last_name()
        booktitle = data_generator.generate_book_name()
        isbn = data_generator.generate_random_integer(5)
        aisle = data_generator.generate_random_integer(3)




        add_book_response = addBook.add_book_to_library(
            name=booktitle,
            isbn=isbn,
            aisle=aisle,
            author=f'{firstname} {lastname}'
        )

        # Check if the request was successful before trying to access the ID
        if add_book_response:
            # Get the ID and save it to a variable
            new_book_id = add_book_response.get("ID")
            assert new_book_id == str(isbn) + str(aisle)

            if new_book_id:
                print(f"\nSuccessfully retrieved new book ID: {new_book_id}")

                # Now you can use this ID in another function call
                # Example: a function to get book details by ID
                # get_book_details(new_book_id)
            else:
                print("\nCould not find 'ID' in the response.")

        response_getBook = getBook.get_book_from_library(new_book_id)

