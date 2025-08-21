# Selenium/Python/Pytest Project Documentation

## Project Overview
pip 

This project is a Selenium-based Page Object Model test automation framework written in Python and utilizing Pytest. It aims to provide a robust and reusable structure for writing and running automated tests.

## Setup Instructions


# Pytest

pytest test_updatecardfromfile.py -v --html=report.html --self-contained-html --headless



# allure

Install:  If you do not have allure installed, run pip install allure-pytest
To run:  pytest --alluredir=allure-results
to generate report allure generate allure-results --clean -o allure-report
to view:  allure open allure-report

pytest test_addcardformvalidationparameter.py -v --alluredir-allure-results
