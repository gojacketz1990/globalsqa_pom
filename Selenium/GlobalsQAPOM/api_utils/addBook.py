# api_utils.py

import requests
import json


def add_book_to_library(name, isbn, aisle, author):
    """
    Sends a POST request to add a book to the library.

    Args:
        name (str): The name of the book.
        isbn (str): The ISBN of the book.
        aisle (str): The aisle number where the book is located.
        author (str): The author of the book.

    Returns:
        dict: The JSON response from the API if successful, otherwise None.
    """
    url = "http://216.10.245.166/Library/Addbook.php"

    payload = {
        "name": name,
        "isbn": isbn,
        "aisle": aisle,
        "author": author
    }

    # The 'requests' library automatically sets the 'Content-Type' header
    # when you use the 'json' parameter, so the 'headers' dictionary is not needed here.

    try:
        response = requests.post(url, json=payload)

        # Check the HTTP status code
        if response.status_code == 200:
            print(f"Request successful for book: '{name}'")
            return response.json()
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(f"Response Body: {response.text}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None