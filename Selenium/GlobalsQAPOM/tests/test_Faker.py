
import pytest
from pages.globalsqa_mainpage import GlobalsqaMainPage
import time
from utilities.FakerHelper import FakerHelper
from utilities.LoggerBase import LoggerBase

class TestFaker(LoggerBase):

    def test_faker(self, logger):
        logger.info("Starting test_faker test")
        # Create an instance of the helper class
        # You can specify a locale if you need data from a different region
        data_generator = FakerHelper(locale='en_US')

        # Generate names
        first_name = data_generator.generate_first_name()
        last_name = data_generator.generate_last_name()
        full_name = data_generator.generate_full_name()
        prefix = data_generator.generate_prefix()

        print(f"First Name: {first_name}")
        print(f"Last Name: {last_name}")
        print(f"Full Name: {full_name}")
        print(f"Prefix: {prefix}")
        print("-----")

        # Generate addresses
        street_address = data_generator.generate_street_address()
        city = data_generator.generate_city()
        state = data_generator.generate_state()
        zipcode = data_generator.generate_zipcode()
        country = data_generator.generate_country()
        full_address = data_generator.generate_full_address()
        web_address = data_generator.generate_website()


        print(f"Street Address: {street_address}")
        print(f"City: {city}")
        print(f"Province/State: {state}")
        print(f"Postal Code: {zipcode}")
        print(f"Country: {country}")
        print(f"Full Address: {full_address}")
        print("-----")

        # Generate other data
        phone_number = data_generator.generate_phone_number()
        email = data_generator.generate_email()
        dob = data_generator.generate_date_of_birth()

        print(f"Phone Number: {phone_number}")
        print(f"Email: {email}")
        print(f"Date of Birth (YYYY-MM-DD): {dob}")
