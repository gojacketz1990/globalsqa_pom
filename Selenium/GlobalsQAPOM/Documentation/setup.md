# Selenium/Python/Pytest Project Documentation

## Project Overview
This project is a Selenium-based Page Object Model test automation framework written in Python and utilizing Pytest. It aims to provide a robust and reusable structure for writing and running automated tests.

## Setup Instructions

### Prerequisites
- Python 3.x
- pip (Python package installer)
- Browser Web Drivers (or run from the web)

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/yourproject.git
    cd yourproject
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv virtual_env_name
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Install WebDriver**:
   - Download the appropriate WebDriver for your browser (e.g., ChromeDriver) and ensure it is in your system PATH or placed in the project directory.

## Usage Examples

### Running Tests

To run all tests, use:
```bash
pytest
```
To run tests in a particular file:
```bash
pytest test_logins.py
```
Run tests by module:
```bash
pytest test_logins.py::test_loginfromexcel
```
Another example specifying a test method in the command line:
```bash
pytest test_mod.py::TestClass::test_method
```
Run tests by marker expressions:
```bash
pytest -m smoke
```
Run tests by keyword expression
```bash
pytest -k "MyClass and not method"
```
Run tests with cutom option:
```bash
pytest --environment_name=chrome
```
Create JUnitXML Format Files
```bash
pytest --junitxml=path

```







