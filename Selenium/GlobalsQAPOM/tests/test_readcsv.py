
import pytest
from pages.globalsqa_mainpage import GlobalsqaMainPage
from utilities.csvReader import CsvReader
import time
import os
from utilities.LoggerBase import LoggerBase

class Testcsv:

    def test_readfromCSV(self):


        # Create an instance of the CsvReader class
        reader = CsvReader('data/data.csv')

        # Read the data from the CSV file
        customer_data = reader.read_data()

        # Check if the data was read successfully
        if customer_data:
            # Print the entire list of dictionaries
            print("All Data:")
            print(customer_data)

            print("\nAccessing a specific row:")
            # Access a specific row (e.g., the second row)
            second_customer = customer_data[1]

            # Access a value by its header name
            print(f"Customer Name: {second_customer['name']}")
            print(f"Customer City: {second_customer['city']}")
            print("")
        if customer_data:
            print("All rows:")
            for row in customer_data:
                print(f"Customer Name: {row['name']}")
                print(f"Customer City: {row['city']}")
                print("")

    def test_writetoCSV(self):
        # This import is fine here, but best practice is at the top of the file
        from utilities.FakerHelper import FakerHelper
        data_generator = FakerHelper(locale='en_US')

        all_customer_data = []
        headers = ['first_name', 'last_name', 'email', 'address', 'phone_number']
        file_name = 'customers.csv'

        for i in range(100):
            record = {
                'first_name': data_generator.generate_first_name(),
                'last_name': data_generator.generate_last_name(),
                'email': data_generator.generate_email(),
                'address': data_generator.generate_full_address(),
                'phone_number': data_generator.generate_phone_number()
            }
            all_customer_data.append(record)

        # CORRECTION 1: Construct the file path FIRST
        csv_file_path = os.path.join('data', file_name)
        print(csv_file_path)

        # CORRECTION 2: Create the CsvReader object just ONCE with the correct path
        csv_writer = CsvReader(csv_file_path)

        # Write the generated data to the CSV file
        csv_writer.write_data(all_customer_data, headers, mode='w')
        #
        # Optional: Read back the data to verify
        print("\nVerifying data written to CSV:")
        read_data = csv_writer.read_data()
        if read_data:
            print(f"Read {len(read_data)} records from {csv_file_path}.")
            # Print the first 3 records for a quick check
            for i, record in enumerate(read_data[:3]):
                print(f"Record {i+1}: {record}")
        else:
            print("Failed to read data back from the CSV file.")
