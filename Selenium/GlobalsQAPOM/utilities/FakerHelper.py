from faker import Faker

class FakerHelper:
    """
    A helper class for generating fake names and addresses using the Faker library.
    """

    def __init__(self, locale='en_US'):
        """
        Initializes the Faker generator with a specific locale.

        Args:
            locale (str): The locale to use for generating fake data (e.g., 'en_US', 'fr_FR').
                          Defaults to 'en_US'.
        """
        self.fake = Faker(locale)

    # --- Name Generation Methods ---

    def generate_first_name(self) -> str:
        """Generates a random first name."""
        return self.fake.first_name()

    def generate_last_name(self) -> str:
        """Generates a random last name."""
        return self.fake.last_name()

    def generate_full_name(self) -> str:
        """Generates a random full name (first and last name)."""
        return self.fake.name()

    def generate_prefix(self) -> str:
        """Generates a random name prefix (e.g., 'Mr.', 'Dr.')."""
        return self.fake.prefix()

    def generate_suffix(self) -> str:
        """Generates a random name suffix (e.g., 'Jr.', 'Sr.')."""
        return self.fake.suffix()

    # --- Address Generation Methods ---

    def generate_street_address(self) -> str:
        """Generates a random street address."""
        return self.fake.street_address()

    def generate_city(self) -> str:
        """Generates a random city name."""
        return self.fake.city()

    def generate_state(self) -> str:
        """Generates a random state name (for the specified locale)."""
        return self.fake.state()

    def generate_zipcode(self) -> str:
        """Generates a random postal code/zip code."""
        return self.fake.postcode()

    def generate_country(self) -> str:
        """Generates a random country name."""
        return self.fake.country()

    def generate_full_address(self) -> str:
        """Generates a complete random address."""
        return self.fake.address()

    # --- Other useful methods (optional additions) ---

    def generate_phone_number(self) -> str:
        """Generates a random phone number."""
        return self.fake.phone_number()

    def generate_email(self) -> str:
        """Generates a random email address."""
        return self.fake.email()

    def generate_date_of_birth(self, min_age=18, max_age=90) -> str:
        """Generates a random date of birth within a given age range."""
        return self.fake.date_of_birth(minimum_age=min_age, maximum_age=max_age).strftime('%Y-%m-%d')


    def generate_website(self):
        """Generates a random website URL."""
        return self.fake.url()
