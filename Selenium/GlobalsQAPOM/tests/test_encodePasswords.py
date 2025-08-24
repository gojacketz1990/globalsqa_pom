
import pytest
import os
from utilities.FakerHelper import FakerHelper # Make sure this path is correct
from utilities.csvReader import CsvReader   # Make sure this path is correct

from utilities.LoggerBase import LoggerBase

class TestEncoding(LoggerBase):

    # In your test file (e.g., test_csv.py or a dedicated setup script)

    def test_writetoCSV(self, logger):
        data_generator = FakerHelper(locale='en_US')

        all_customer_data = []
        headers = ['first_name', 'last_name', 'username', 'encoded_password', 'email', 'address', 'phone_number']
        file_name = 'customers_PW_encoded.csv'

        for i in range(100):
            first_name = data_generator.generate_first_name()
            last_name = data_generator.generate_last_name()

            # Concatenate the first name and last name with a period
            username = f"{first_name.lower()}.{last_name.lower()}"

            record = {
                'first_name': first_name,
                'last_name': last_name,
                'username': username,
                'encoded_password': data_generator.encode_plaintext(data_generator.generate_strong_password()),
                'email': data_generator.generate_email(),
                'address': data_generator.generate_full_address(),
                'phone_number': data_generator.generate_phone_number()
            }
            all_customer_data.append(record)

        # Use os.path.join() to create the platform-independent file path
        csv_file_path = os.path.join('./data', file_name)
        print(f"Writing to: {csv_file_path}")

        # Create the CsvReader object with the correct path string
        csv_writer = CsvReader(csv_file_path)

        # Write the generated data to the CSV file
        csv_writer.write_data(all_customer_data, headers, mode='w')

        # --- Verification Section (Optional but Recommended) ---
        print("\nVerifying data written to CSV:")
        read_data = csv_writer.read_data()

        if read_data:
            print(f"Read {len(read_data)} records from {csv_file_path}.")

            # Print the first 3 records for a quick check
            for i, record in enumerate(read_data[:3]):
                print(f"Record {i+1}: {record}")

            # Read back and decode a sample to verify
            print("\nVerifying a sample user from the CSV:")
            sample_user = read_data[0]
            decoded_password = data_generator.unencode(sample_user['encoded_password'])
            print(f"Read Username: {sample_user['username']}, Decoded Password: {decoded_password}")
        else:
            print("Failed to read data back for verification.")





    def test_readfromCSV(self):
        # Create an instance of the CsvReader class
        data_generator = FakerHelper(locale='en_US')
        reader = CsvReader('data/customers_PW_encoded.csv')

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
            print(f"Customer Name: {second_customer['username']}")
            print(f"Customer City: {second_customer['encoded_password']}")
            decoded_password = data_generator.unencode(second_customer['encoded_password'])
            print(f"Read Username: {second_customer['username']}, Decoded Password: {decoded_password}")
            print("")
        if customer_data:
            print("All rows:")
            for row in customer_data:
                print(f"Customer username: {row['username']}")
                print(f"Customer encoded_password: {row['encoded_password']}")
                decoded_password = data_generator.unencode(row['encoded_password'])
                print(f"Read Username: {row['username']}, Decoded Password: {decoded_password}")
                print("")
