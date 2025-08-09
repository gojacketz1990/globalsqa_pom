import pytest

driver = None
import os
from selenium import webdriver


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
        driver = webdriver.Chrome()
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
