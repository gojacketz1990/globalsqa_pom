# Selenium/Python/Pytest Project Documentation

## Project Overview
This project is a Selenium-based Page Object Model test automation framework written in Python and utilizing Pytest. It aims to provide a robust and reusable structure for writing and running automated tests.

## Setup Instructions

### Prerequisites
- The application being tested here has a header that contains shared links that are available from every page
- To handle this, we have created a "header page".  When header page is called and a link is clicked, the new page is instantiated in the header page
- and returned to the test script dynamically.


### Explanation

1. **Shared Headers**:
    ```bash
    git clone https://github.com/yourusername/yourproject.git
    cd yourproject
    ```
