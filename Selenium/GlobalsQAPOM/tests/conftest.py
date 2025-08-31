import pytest
import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# ----------------------------------------------------------------------------------
# This is the code that needs to be at the top of the file to fix the path
# ----------------------------------------------------------------------------------
# Get the path to the directory containing this conftest.py file ('tests')
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the path to the project root (one directory up from 'tests')
project_root = os.path.abspath(os.path.join(current_dir, '..'))

# Insert the project root path at the beginning of the system path
# This ensures Python can find 'utilities' and other modules
sys.path.insert(0, project_root)

# The import statement now works because the path has been fixed
from utilities.logger_setup import setup_test_logger

driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Browser to run tests on (chrome, firefox, safari)"
    )
    parser.addoption(
        "--environment_name", action="store", default="QA", help="Environment to test against (QA, UAT)"
    )
    parser.addoption(
        "--headless", action="store_true", default=False, help="Run tests in headless mode"
    )

@pytest.fixture(scope="function")
def setup_globalsqa(request):

    global driver
    browser_name = request.config.getoption("browser_name")
    print("Browser:")
    print(browser_name)
    if browser_name.lower() == "chrome":
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)
    elif browser_name.lower() == "firefox":
        driver = webdriver.Firefox()
    elif browser_name.lower() == "safari":
        driver = webdriver.Safari()
    else:
        print("reap it")

    environment_name = request.config.getoption("environment_name")
    print("Environment:")
    print(environment_name)
    if environment_name == "QA":
        driver.get("https://www.globalsqa.com/")

    elif environment_name == "UAT":
        driver.get("https://www.globalsqa.com/")


    driver.maximize_window()
    request.cls.driver = driver

    # tear down
    yield
    driver.close()

@pytest.fixture(scope="function")
def logger(request):
        """
        Fixture to provide a logger instance named after the current test function.
        """
        # Get the test function's name
        test_name = request.node.name

        # Set up and return the logger
        return setup_test_logger(test_name)