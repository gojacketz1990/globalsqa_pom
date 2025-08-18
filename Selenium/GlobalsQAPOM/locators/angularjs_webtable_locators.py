class AngularJSWebTablePageLocators():

    first_name_search_locator = [
        ("css","input[st-search='firstName']")
    ]

    global_search_locator = [
        ("css","input[placeholder='global search']")
    ]

    # Locator for the entire table body
    table_locator = [("css", "table")]

    # Locator for a single row within the table body
    row_locator = [("tag_name", "tr")]

    # Locator for a single cell within a row
    cell_locator = [("tag_name", "td")]

    # This is a dynamic locator template to find a cell containing the user's name
    user_first_name_in_table_locator = [
        ("xpath", "//td[normalize-space()='{}']")
    ]

    user_full_name_locator = [
        ("xpath", "//tr[normalize-space(td[1])='{}' and normalize-space(td[2])='{}']")
    ]

    # Locator for the table body, assumed to be inside the table_locator
    table_body_locator = [("xpath", "//tbody")]
    # Locator for a single table row inside the table body
    table_row_locator = [("xpath", "./tr")]
    # Locator for a single table cell inside a row
    table_cell_locator = [("xpath", "./td")]
    # Dynamic locator for a table header based on its text

    table_header_locator = [("xpath", "//th[text()='{}']")]
