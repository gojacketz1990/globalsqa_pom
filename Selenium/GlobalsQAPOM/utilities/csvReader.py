import csv
import os

class CsvReader:
    """A class to read data from a CSV file with headers."""

    def __init__(self, file_path):
        """Initializes the CsvReader with a file path."""
        self.file_path = file_path

    def read_data(self):
        """
        Reads the CSV file and returns its content as a list of dictionaries.
        Each dictionary's keys correspond to the CSV headers.
        """
        data = []
        try:
            with open(self.file_path, 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    data.append(row)
        except FileNotFoundError:
            print(f"Error: The file at {self.file_path} was not found.")
            return None
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            return None

        return data

    def write_data(self, data: list, headers: list, mode='w'):
        """
        Writes data (a list of dictionaries) to the CSV file.
        The 'mode' can be 'w' for write or 'a' for append.
        """
        try:
            # Ensure the directory exists before writing
            directory = os.path.dirname(self.file_path)
            if directory and not os.path.exists(directory):
                os.makedirs(directory)
                print(f"Created directory: {directory}")

            with open(self.file_path, mode, newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=headers)

                # Write the header row only if in 'write' mode ('w')
                if mode == 'w':
                    writer.writeheader()

                # Write all the data rows
                writer.writerows(data)
                print(f"Successfully wrote {len(data)} records to {self.file_path} in '{mode}' mode.")

        except Exception as e:
            print(f"An error occurred while writing to the file: {e}")
