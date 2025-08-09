# Selenium/Python Project Documentation

## Method Usage
This project is a Selenium-based test Page Object Model automation framework written in Python. It aims to provide a robust and reusable structure for writing and running automated tests.

## BasePage Methods 

### _get_by_method(locator_type)
- This method will never be called directly but gets called by other methods.
- The method converts the locator type from the locator dictionary by looking up the 
- type from the locators from page classes such as LoginPage.  LoginPage sends a dictionary 
- locator such as ("id", "login-button"), the _get_by_method takes the "id" and converts that to 
- "By.ID" from the dictionary.

### get_element(locators)
- This method will find a single web element using the locator dictionary (with self healing locators)
- The method will return the element if found
- If not found, an error will be raised.
- 
### get_elements(locators)
- This method will multiple web elements using the locator dictionary (with self healing locators)
- The method will return the list of elements if found
- If not found, an error will be raised.

### get_child_element(parent_element, locators)
- This method will find a child element from a given parent element by chaining the elements together.
- The element is then returned
- If not found, an error will be raised

### type_into_element(self, text, locators):
- This method locates a web element, clicks in it, clears it then types the given text into it

### element_click(locators)
- Clicks a web element found using a list of locator strategies.

### wait_presence_element(locators, timeout=10)
- Waits for an element to be present using a list of locator strategies.

### retrieve_child_element_text(parent_element, locators)
- Retrieves text from a child element given its parent element as input by using chaining.


### wait_and_click_element(locators)
- Waits for an element to be present and clicks it
- If not found, an error will be raised


### - element_child_click(parent_element, locators)
- Clicks on a child element given its parent element as input.


### - retrieve_element_text(locators)
- Retrieves text from an element found using a list of locator strategies.

### - check_display_status_of_element(locators)
- Checks if an element is displayed.
- Returns boolean
- 
### - get_response_code(url)
- Gets the HTTP response code from a URL.

### - wait_for_element_to_be_visible(locators)
- Waits for a web element to be visible.
- If it is visible, the element is returned
- If not found, an error will be raised

### - is_element_present(locators)
- Checks if an element is present
- Returns boolean

### - select_from_dropdown_by_visible_text(locators, text)
- Selects an option from a dropdown by visible text.

### - hover_over_element(locators)
- Hovers over an element using ActionChains move_to_element

### - switch_to_frame(locators)
- Switches from the default content to a frame/iframe.
- The context and actions now take place in the new frame.

### - switch_to_default_content()
- Switches to the default content from a frame.
- The context and actions now take place in the original content

### - get_element_attribute(locators, attribute)
- Returns an attribute value given an attribute.  
- Values come from the elements CSS properties
- This can be used to check formatting, color, etc.



## BaseTest Methods 

### create_emallAddress(self)
- Generates a dummy email address with a unique timestamp to ensure uniqueness.

### getLogger(cls)
- Sets up and returns a logger for the class. Ensures that only one logger is created per class.

### unencode(self, todecode)
- Decodes a base64 encoded string
- Returns the decoded string
- Usage is mostly for passwords that you have encoded, they must be unencoded to use as credentials

### encodeplaintext(cls, toencode):
- Takes a plain text string and encodes it to base64
- Returns the base64 encoded strong


## ReadConfiguration Methods 

### read_configuration(category,key)
- Method to read from a configuration file given the Category and Key
- Returns a string
- Throws an error if category or key are not found

## readFromExcel Methods

### get_row_count(path, sheet_name)
- Retrieves the total number of rows in a specified Excel sheet.
- Input is path to file and sheet name

### get_column_count(path, sheet_name)
- Retrieves the total number of columns in a specified Excel sheet.
- Input is path to file and sheet name

### get_cell_data(path, sheet_name, row_number, column_number)
- Retrieves the value of a specified cell in an Excel sheet.
- Input is path to file, sheet name, row and column.

### set_cell_data(path, sheet_name, row_number, column_number, data)
- Sets the value of a specified cell in an Excel sheet.
- Input is path to file, sheet name, row, column and the value.

### get_data_from_excel(path, sheet_name)
- Retrieves all data from a specified Excel sheet as a list of lists, starting from the second row.
- Returns list of lists containing the data


## excelDataBuild Methods

### createencodedfile(inputFilePath,inputSheet,exportFilePath,exportSheet)
- Takes a file with plain text and converts it to base64
- This should be used only as a data building method
- Input is input file path, input sheet, export file path and export sheet
- Output is a file with usernames and passwords encoded in base64 for security.
