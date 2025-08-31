# api_utils.py

import requests
import json


def get_book_from_library(book_id):
    """
    Sends a GET request to retrieve a book from the library by its ID.

    Args:
        book_id (str): The unique ID of the book to retrieve.

    Returns:
        dict: The JSON response from the API if successful, otherwise None.
    """
    # The URL now uses the provided book_id as a query parameter
    url = f"http://216.10.245.166/Library/GetBook.php?ID={book_id}"

    # No payload is needed for a GET request

    try:
        # Use requests.get() instead of requests.post()
        response = requests.get(url)

        # Check the HTTP status code
        if response.status_code == 200:
            print(f"Request successful for book with ID: {book_id}")
            print("\nFull Response Body:")
            print(response.text)  # This will print the full response as a string
            print("--------------------\n")
            return response.json()  # Return the full JSON response
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(f"Response Body: {response.text}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None