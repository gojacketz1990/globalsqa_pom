# Parser Options

## environment_name
The pytest option --environment_name can be passed in as an argument at run time.  The environments are set up in the conftest.ini setup_and_teardown fixture.
The system will read the input and select the appropriate environment to run the tests in.

Valid environments right now:
- QA
- UAT

If no input is given, the default is QA.

## browser_name

The pytest option --browser_name can be passed in as an argument at run time.  The environments are set up in the conftest.ini setup_and_teardown fixture.
The system will read the input and select the appropriate browser to run the tests in.

Valid browsers: 
- chrome
- firefox
- safari

If no input is given, the default is chrome.
